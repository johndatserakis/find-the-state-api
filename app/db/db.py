import os
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, create_engine
from sqlalchemy.sql import func
from databases import Database

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")

if POSTGRES_USER is None:
    raise ValueError("Incorrect database credentials")

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
