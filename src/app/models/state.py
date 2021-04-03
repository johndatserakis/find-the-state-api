import datetime
from pydantic import BaseModel


class StateBase(BaseModel):
    name: str
    summary: str
    link: str
    image: str


class State(StateBase):
    id: int
    created_date: datetime.datetime
