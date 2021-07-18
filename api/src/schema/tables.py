import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, TIMESTAMP, ForeignKey, Float, Integer, TIME, Boolean, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

YoutubeBaseTable = declarative_base()


class UserTable(YoutubeBaseTable):
    """
    Define User database table ORM model
    """
    __tablename__ = "users"
    __table_args__ = {"schema": "youtube"}

    # Register columns
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, primary_key=True, index=True)
    name = Column(String(200), unique=False, index=True)
    mail = Column(String(200), unique=True)
    password = Column(String(200))
