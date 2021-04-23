from pydantic import BaseModel
import datetime
import uuid


class ScoreBase(BaseModel):
    score: str


class Score(ScoreBase):
    id: uuid.UUID
    created_date: datetime.datetime


class ScoreCreate(ScoreBase):
    pass


class ScoreUpdate(ScoreBase):
    pass


class ScoreDelete(BaseModel):
    id: uuid.UUID
