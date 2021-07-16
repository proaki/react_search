import os
import sys

sys.path.insert(0, os.getcwd())
from alembic.command import upgrade
from alembic.config import Config
from src.utils.custom_error_handlers import DBError
from src.utils.common_logger import logger
import pkg_resources


class DBUpgrade:
    @staticmethod
    def upgrade():
        """
        This executes upgrade DB metadata based on ORM models defined by SQL Alchemy
        It runs the latest (head) version of Alembic generated script in insights/versions/{hashed_value.py}
        :return success: True if it succeeded
        """
        success = False
        try:
            filepath = pkg_resources.resource_filename("src", "alembic.ini")
            upgrade(Config(filepath), "head")
            logger.info("Successfully upgraded DB")
            success = True
        except Exception as err:
            logger.error(f"Failed to upgrade DB: {err}")
            raise DBError(message=f"Failed to upgrade DB: {err}")
        finally:
            return success


if __name__ == "__main__":
    DBA = DBUpgrade()
    logger.info("Upgrading database")
    DBA.upgrade()
    logger.info("Successfully upgraded database")