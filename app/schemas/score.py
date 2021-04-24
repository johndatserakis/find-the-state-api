from pydantic import BaseModel, StrRegexError, validator
import datetime
import uuid
import re


class ScoreBase(BaseModel):
    score: str

    @validator("score")
    def matches_regex(cls, v):
        regex = r"\d\d:\d\d:\d\d"
        if not re.match(regex, v):
            raise StrRegexError(pattern=regex)
        return v


class Score(ScoreBase):
    id: uuid.UUID
    created_date: datetime.datetime


class ScoreCreate(ScoreBase):
    token: str


class ScoreUpdate(ScoreBase):
    pass


class ScoreDelete(BaseModel):
    id: uuid.UUID
