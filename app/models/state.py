from sqlalchemy import Table
from db.db import SQLALCHEMY_DATABASE_URL, engine, metadata

states = Table("states", metadata, autoload=True, autoload_with=engine)
