from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    summary = Column(String)
    link = Column(String)
    image = Column(String)
    created_date = Column(DateTime, default=func.now(), nullable=False)
