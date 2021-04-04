from db.db import database
from models.state import states as table
from schemas.state import StateCreate, StateUpdate
from sqlalchemy import literal_column
from sqlalchemy.sql import func
import uuid


async def get(id: uuid.UUID):
    return await get_by_id(id)


async def get_by_id(id: uuid.UUID):
    query = table.select().where(id == table.c.id)
    return await database.fetch_one(query=query)


async def get_by_name(name: str):
    query = table.select().where(name == table.c.name)
    return await database.fetch_one(query=query)


async def get_all():
    query = table.select()
    return await database.fetch_all(query=query)


async def create(payload: StateCreate):
    query = table.insert().values(
        name=payload.name,
        summary=payload.summary,
        link=payload.link,
        image=payload.image,
    )
    return await database.execute(query=query)


async def update(id: uuid.UUID, payload: StateUpdate):
    query = (
        table.update()
        .where(id == table.c.id)
        .values(
            name=payload.name,
            summary=payload.summary,
            link=payload.link,
            image=payload.image,
            updated_date=func.now(),
        )
        .returning(table.c.id)
    )
    return await database.execute(query=query)


async def delete(id: uuid.UUID):
    query = table.delete().where(id == table.c.id)
    return await database.execute(query=query)
