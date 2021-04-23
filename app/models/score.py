from sqlalchemy import Table
from db.db import SQLALCHEMY_DATABASE_URL, engine, metadata

scores = Table("scores", metadata, autoload=True, autoload_with=engine)
