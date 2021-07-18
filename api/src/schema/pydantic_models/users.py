from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    """
    User database table schema
    It holds all column names and relationship to other tables
    """
    name: str
    mail: str
    password: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    """
    Fields information needed for POST
    """
    name: str
    mail: str
    password: str


class UserUpdate(BaseModel):
    """
    Fields information needed for Update
    """
    id: Optional[str]
    name: str
    mail: str
    password: str


class UserDelete(BaseModel):
    """
    Fields information needed for Delete
    """
    id: Optional[str]
    mail: str
