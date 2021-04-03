from app.models import StateSchema
from app.db import states, database


async def get(name: str):
    query = states.select().where(name == states.c.name)
    return await database.fetch_one(query=query)


async def get_all():
    query = states.select()
    return await database.fetch_all(query=query)
