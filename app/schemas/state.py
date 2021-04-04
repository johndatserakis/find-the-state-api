from pydantic import BaseModel
import datetime
import uuid


class StateBase(BaseModel):
    name: str
    summary: str
    link: str
    image: str


class State(StateBase):
    id: uuid.UUID
    created_date: datetime.datetime


class StateCreate(StateBase):
    pass


class StateUpdate(StateBase):
    pass


class StateDelete(BaseModel):
    id: uuid.UUID
