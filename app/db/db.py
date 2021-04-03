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

# # Build tables
# states = Table(
#     "states",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("summary", String),
#     Column("link", String),
#     Column("image", String),
#     Column("created_date", DateTime, default=func.now(), nullable=False),
# )

# databases query builder
database = Database(SQLALCHEMY_DATABASE_URL)
