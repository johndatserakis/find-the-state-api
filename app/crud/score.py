from db.db import database
from models.score import scores as table
from schemas.score import ScoreCreate, ScoreUpdate
from sqlalchemy import literal_column
from sqlalchemy.sql import func
import uuid


async def get(id: uuid.UUID):
    query = table.select().where(id == table.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = table.select()
    return await database.fetch_all(query=query)


async def create(payload: ScoreCreate):
    query = table.insert().values(score=payload.score, streak_high=payload.streak_high)
    return await database.execute(query=query)


async def update(id: uuid.UUID, payload: ScoreUpdate):
    query = (
        table.update()
        .where(id == table.c.id)
        .values(
            score=payload.score,
            updated_date=func.now(),
        )
        .returning(table.c.id)
    )
    return await database.execute(query=query)


async def delete(id: uuid.UUID):
    query = table.delete().where(id == table.c.id)
    return await database.execute(query=query)
