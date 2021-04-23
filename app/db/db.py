import os
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, create_engine
from sqlalchemy.sql import func
from databases import Database
from utils.env import get_settings

POSTGRES_USER = get_settings().postgres_user
POSTGRES_PASSWORD = get_settings().postgres_password
POSTGRES_HOST = get_settings().postgres_host
POSTGRES_DB = get_settings().postgres_db

try:
    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
except Exception:
    raise ValueError("Error connecting to database")

# SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"options": "-c timezone=utc"}
)
metadata = MetaData()

# databases query builder
database = Database(SQLALCHEMY_DATABASE_URL)
