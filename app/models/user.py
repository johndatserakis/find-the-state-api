import sqlalchemy
from fastapi_users import models
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from schemas.user import UserDB
from db.db import database
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()

# Table name handling https://github.com/frankie567/fastapi-users/issues/581#issue-846915260
class UserTable(Base, SQLAlchemyBaseUserTable):
    __tablename__ = "users"


users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)
