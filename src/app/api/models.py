from pydantic import BaseModel, Field


class StateSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    summary: str = Field(..., min_length=3, max_length=10000)
    link: str = Field(..., min_length=3, max_length=1000)
    image: str = Field(..., min_length=3, max_length=1000)


class StateDB(StateSchema):
    id: int
