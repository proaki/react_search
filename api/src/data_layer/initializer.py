import os
import sys
sys.path.insert(0, os.getcwd())
import contextlib
from sqlalchemy import MetaData
from sqlalchemy.schema import CreateSchema
from sqlalchemy_utils import database_exists, create_database
from src.utils.custom_error_handlers import DBError
from src.settings import load_config
from src.data_layer.base import DBConnector
from src.data_layer.db_upgrade import DBUpgrade
from src.utils.common_logger import logger
from src.schema.tables import YoutubeBaseTable


class DBInitializer:

    def __init__(self, declarative_bases=None):

        if declarative_bases is None:
            self.declarative_bases = [YoutubeBaseTable]
        else:
            self.declarative_bases = declarative_bases

        load_config("../.env")

        self.DBC = DBConnector()
        self.BaseTable = MetaData()

        for declarative_base in self.declarative_bases:
            for (table_name, table) in declarative_base.metadata.tables.items():
                self.BaseTable._add_table(table_name, table.schema, table)

        self.engine = self.DBC.engine

    def check_database_exist(self):
        """
        Check if database already exists
        :return True if database already exists
        """
        return database_exists(self.engine.url)

    def create_database(self):
        """
        Create database if it does not exist
        :return success: True if it succeeded or if database already exists
        """
        # Create database if it does not exist
        status = False
        if database_exists(self.engine.url):
            logger.info("Database already exists. Skipping")
            status = True
            return status
        try:
            create_database(self.engine.url)
            status = True
        except Exception as err:
            logger.info(f"Failed to create database: {err}")
            raise DBError(message=f"Failed to create database: {err}")
        finally:
            return status

    def check_schema_exists(self, schema_name: str):
        """
        Check if schema already exists
        :return True if schema already exists
        """
        return (
            True
            if schema_name in self.engine.dialect.get_schema_names(self.engine)
            else False
        )

    def create_schema(self, schema_name: str):
        """
        Create schema from given schema name
        :return success: True if it succeeded
        """
        status = False
        try:
            self.engine.execute(CreateSchema(schema_name))
            status = True
        except Exception as err:
            logger.info(f"Failed to create schema: {err}")
            raise DBError(message=f"Failed to create schema: {err}")
        finally:
            return status

    def create_schemas(self):
        """
        Create schemas
        :return success: True if it succeeded
        """
        status = False
        try:
            if os.getenv(
                    "YOUTUBE_DB_SCHEMA"
            ) not in self.engine.dialect.get_schema_names(self.engine):
                self.engine.execute(CreateSchema(os.getenv("YOUTUBE_DB_SCHEMA")))
            logger.info("Successfully created all schemas")
            status = True
        except Exception as err:
            logger.info(f"Failed to create schemas: {err}")
            raise DBError(message=f"Failed to create schemas: {err}")
        finally:
            return status

    def create_tables(self):
        """
        Create tables
        :return success: True if it succeeded
        """
        status = False
        try:
            self.BaseTable.create_all(self.engine)
            status = True
        except Exception as err:
            logger.info(f"Failed to create tables: {err}")
            raise DBError(message=f"Failed to create tables: {err}")
        finally:
            return status

    def drop_tables(self):
        """
        Create tables if they do not exist
        :return success: True if it succeeded
        """
        success = False
        try:
            self.BaseTable.drop_all(self.engine)
            success = True
        except Exception as err:
            logger.info(f"Failed to drop tables: {err}")
            raise DBError(message=f"Failed to drop tables: {err}")
        finally:
            return success

    def drop_table_contents(self):
        """
        Drop all contents from all tables
        :return success: True if it succeeded
        """
        success = False
        try:
            with contextlib.closing(self.engine.connect()) as con:
                trans = con.begin()
                for table in reversed(self.BaseTable.sorted_tables):
                    con.execute(table.delete())
                trans.commit()
            success = True
        except Exception as err:
            logger.info("Failed to drop table contents")
            raise DBError(message=f"Failed to drop tables contents {err}")
        finally:
            return success


def process_db(
        declarative_bases=[YoutubeBaseTable],
        schemas=["youtube"],
):
    """
    Run DB initializer and upgrade
    """
    DBI = DBInitializer(declarative_bases)

    # Create database if it doesn't exist
    if DBI.check_database_exist():
        logger.info("Database already exists. Skipping initialization")
    else:
        logger.info("Initializing database")
        drop_status = DBI.drop_tables()
        if drop_status is True:
            logger.info(f"Successfully dropped all tables")
        create_db_status = DBI.create_database()
        if create_db_status is True:
            logger.info("Successfully created database")

    # Create schema if it doesn't exist
    init_schema = False
    for schema in schemas:
        if DBI.check_schema_exists(schema):
            logger.info(f"{schema} already exists. Skipping initialization")
        else:
            logger.info(f"Creating {schema}")
            create_schema_status = DBI.create_schema(schema)
            if create_schema_status:
                logger.info(f"Successfully created {schema}")

            init_schema = True

    # Create tables and initial source if db was initialized
    if init_schema is True:
        create_tables_status = DBI.create_tables()
        if create_tables_status:
            logger.info("Successfully created all tables")

        logger.info("Successfully initialized database")

    # Upgrade DB
    DBA = DBUpgrade()
    logger.info("Upgrading database")
    DBA.upgrade()
    logger.info("Successfully upgraded database")


if __name__ == "__main__":
    process_db()