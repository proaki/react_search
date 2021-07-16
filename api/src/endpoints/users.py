from typing import List
import sqlalchemy
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Response
from ..utils.common_logger import logger
from ..schemas.users import UserSchema, UserCreate, UserUpdate, UserDelete
from ..models.db_models import UserModel
from . import DBC
router = APIRouter()


@router.get("/users", response_model=List[UserSchema])
def get_all_users(db: Session = Depends(DBC.get_session)):
    """
    GET all users
    :param db: DB session
    :return: ALl user entries
    """
    return db.query(UserModel).all()


@router.get("/users/name/{user_mail}", response_model=UserSchema)
def get_one_user_by_mail(user_mail: str, db: Session = Depends(DBC.get_session)):
    """
    GET one user by user_id
    :param user_mail: User mail to get
    :param db: DB session
    :return: Retrieved user entry
    """
    try:
        # Get user by ID
        return db.query(UserModel).filter(UserModel.mail == user_mail).one()
    except sqlalchemy.orm.exc.NoResultFound:
        raise Exception(f"{user_mail} does not exist")


@router.get("/users/id/{user_id}", response_model=UserSchema)
def get_one_user_by_id(user_id: str, db: Session = Depends(DBC.get_session)):
    """
    GET one user by ID
    :param user_id: User ID to get
    :param db: DB session
    :return: Retrieved user entry
    """
    try:
        # Get user by name
        return db.query(UserModel).filter(UserModel.id == user_id).one()
    except sqlalchemy.orm.exc.NoResultFound:
        raise Exception(f"{user_id} does not exist")


@router.post("/users")
def post_one_user(user: UserCreate, db: Session = Depends(DBC.get_session)):
    """
    POST one user
    It reads parameters from the request field and add missing fields from default values defined in the model
    :param user: UserBase class that contains all columns in the table
    :param db: DB session
    :return: Created user entry
    """
    try:
        # Create User Model
        user_to_create = UserModel(**user.dict())

        # Commit to DB
        db.add(user_to_create)
        db.commit()
        db.refresh(user_to_create)
        return Response(200)
    except Exception as err:
        logger.error(f"Failed to create user: {err}")


@router.put("/users")
def put_one_user(user: UserUpdate, db: Session = Depends(DBC.get_session)):
    """
    PUT one user
    It reads parameters from the request field and update finds the entry and update it
    :param user: UserUpdate class that contains requested field to update
    :param db: DB session
    :return: Updated user entry
    """
    try:
        # Get user by ID
        user_to_put = db.query(UserModel).filter(UserModel.mail == user.mail).one()

        # Update model class variable for requested fields
        for var, value in vars(user).items():
            setattr(user_to_put, var, value) if value else None

        # Commit to DB
        db.add(user_to_put)
        db.commit()
        db.refresh(user_to_put)
        return Response(200)
    except sqlalchemy.orm.exc.NoResultFound:
        raise Exception(f"{user.id} does not exist")
    except Exception as err:
        raise Exception(f"Failed to update user: {err}")

@router.delete("/users/id/{user_mail}", response_model=UserDelete)
def delete_one_user_by_id(user_mail: str, db: Session = Depends(DBC.get_session)):
    """
    DELETE one user by ID
    It reads parameters from the request field, finds the entry and delete it
    :param user_mail: User mail address to delete
    :param db: DB session
    :return: Deleted user entry
    """
    try:
        # Delete entry
        affected_rows = db.query(UserModel).filter(UserModel.mail == user_mail).delete()
        if not affected_rows:
            raise sqlalchemy.orm.exc.NoResultFound
        # Commit to DB
        db.commit()
        return Response(200)
    except sqlalchemy.orm.exc.NoResultFound:
        raise Exception(f"{user_mail} does not exist")
    except Exception as err:
        raise Exception(f"Failed to delete user: {err}")
