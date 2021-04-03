from typing import List, Optional

from pydantic import BaseModel


class StateBase(BaseModel):
    name: str
    summary: str
    link: str
    image: str
    created_date: str


class StateCreate(StateBase):
    pass


class State(StateBase):
    id: int

    class Config:
        orm_mode = True
