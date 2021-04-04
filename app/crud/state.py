from db.db import database
from models.state import states
from schemas.state import StateCreate, StateUpdate
import uuid
from sqlalchemy import literal_column
from sqlalchemy.sql import func


async def get(id: uuid.UUID):
    return await get_by_id(id)


async def get_by_id(id: uuid.UUID):
    query = states.select().where(id == states.c.id)
    return await database.fetch_one(query=query)


async def get_by_name(name: str):
    query = states.select().where(name == states.c.name)
    return await database.fetch_one(query=query)


async def get_all():
    query = states.select()
    return await database.fetch_all(query=query)


async def create(payload: StateCreate):
    query = states.insert().values(
        name=payload.name,
        summary=payload.summary,
        link=payload.link,
        image=payload.image,
    )
    return await database.execute(query=query)


async def update(id: uuid.UUID, payload: StateUpdate):
    query = (
        states.update()
        .where(id == states.c.id)
        .values(
            name=payload.name,
            summary=payload.summary,
            link=payload.link,
            image=payload.image,
            updated_date=func.now(),
        )
        .returning(states.c.id)
    )
    return await database.execute(query=query)


async def delete(id: uuid.UUID):
    query = states.delete().where(id == states.c.id)
    return await database.execute(query=query)
