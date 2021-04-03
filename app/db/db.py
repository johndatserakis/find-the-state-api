import os
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, create_engine
from sqlalchemy.sql import func
from databases import Database

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
)

# SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

# Attach all tables built by migrations here
states = Table("states", metadata, autoload=True, autoload_with=engine)

# databases query builder
database = Database(SQLALCHEMY_DATABASE_URL)
