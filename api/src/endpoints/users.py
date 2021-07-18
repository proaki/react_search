from typing import List
import sqlalchemy
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Response, status
from src.utils.common_logger import logger
from src.schema.pydantic_models.users import UserSchema, UserCreate, UserUpdate, UserDelete
from src.schema.tables import UserTable
from . import DBC
router = APIRouter()


@router.get("/users", response_model=List[UserSchema])
def get_all_users(db: Session = Depends(DBC.get_session)):
    """
    GET all users
    :param db: DB session
    :return: ALl user entries
    """
    return db.query(UserTable).all()


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
        return db.query(UserTable).filter(UserTable.mail == user_mail).one()
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
        return db.query(UserTable).filter(UserTable.id == user_id).one()
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
        user_to_create = UserTable(**user.dict())

        # Commit to DB
        db.add(user_to_create)
        db.commit()
        db.refresh(user_to_create)
        return Response(200)
    except Exception as err:
        logger.error(f"Failed to create user: {err}")


@router.put("/users/id/{user_id}")
def put_one_user_by_id(user: UserUpdate, response: Response, db: Session = Depends(DBC.get_session)):
    """
    PUT one user by user ID
    It reads parameters from the request field and update finds the entry and update it
    :param user: UserUpdate class that contains requested field to update
    :param response: Response
    :param db: DB session
    :return: Updated user entry
    """
    try:
        # Get user by ID
        user_to_put = db.query(UserTable).filter(UserTable.id == user.id).one()

        # Update model class variable for requested fields
        for var, value in vars(user).items():
            setattr(user_to_put, var, value) if value else None

        # Commit to DB
        db.add(user_to_put)
        db.commit()
        db.refresh(user_to_put)
        response.status_code = status.HTTP_200_OK
        return user_to_put
    except sqlalchemy.orm.exc.NoResultFound:
        raise Exception(f"{user.id} does not exist")
    except Exception as err:
        raise Exception(f"Failed to update user: {err}")


@router.put("/users/mail/{user_mail}")
def put_one_user_by_mail(user: UserUpdate, response: Response, db: Session = Depends(DBC.get_session)):
    """
    PUT one user by user mail
    It reads parameters from the request field and update finds the entry and update it
    :param user: UserUpdate class that contains requested field to update
    :param response: Response
    :param db: DB session
    :return: Updated user entry
    """
    try:
        # Get user by ID
        user_to_put = db.query(UserTable).filter(UserTable.mail == user.mail).one()

        # Update model class variable for requested fields
        for var, value in vars(user).items():
            setattr(user_to_put, var, value) if value else None

        # Commit to DB
        db.add(user_to_put)
        db.commit()
        db.refresh(user_to_put)
        response.status_code = status.HTTP_200_OK
        return user_to_put
    except sqlalchemy.orm.exc.NoResultFound:
        raise Exception(f"{user.mail} does not exist")
    except Exception as err:
        raise Exception(f"Failed to update user: {err}")


@router.delete("/users/id/{user_id}", response_model=UserDelete)
def delete_one_user_by_id(user_id: str, response: Response, db: Session = Depends(DBC.get_session)):
    """
    DELETE one user by ID
    It reads parameters from the request field, finds the entry and delete it
    :param user_id: User ID to delete
    :param response: Response
    :param db: DB session
    :return: Deleted user entry
    """
    try:
        # Delete entry
        affected_rows = db.query(UserTable).filter(UserTable.id == user_id).delete()
        if not affected_rows:
            raise sqlalchemy.orm.exc.NoResultFound
        # Commit to DB
        db.commit()
        response.status_code = status.HTTP_200_OK
        return {"user_id": user_id}
    except sqlalchemy.orm.exc.NoResultFound:
        raise Exception(f"{user_id} does not exist")
    except Exception as err:
        raise Exception(f"Failed to delete user: {err}")


@router.delete("/users/mail/{user_mail}", response_model=UserDelete)
def delete_one_user_by_id(user_mail: str, response: Response, db: Session = Depends(DBC.get_session)):
    """
    DELETE one user by mail
    It reads parameters from the request field, finds the entry and delete it
    :param user_mail: User mail address to delete
    :param response: Response
    :param db: DB session
    :return: Deleted user entry
    """
    try:
        # Delete entry
        affected_rows = db.query(UserTable).filter(UserTable.mail == user_mail).delete()
        if not affected_rows:
            raise sqlalchemy.orm.exc.NoResultFound
        # Commit to DB
        db.commit()
        response.status_code = status.HTTP_200_OK
        return {"mail": user_mail}
    except sqlalchemy.orm.exc.NoResultFound:
        raise Exception(f"{user_mail} does not exist")
    except Exception as err:
        raise Exception(f"Failed to delete user: {err}")
