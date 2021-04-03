from db.db import states, database


async def get_by_id(id: int):
    query = states.select().where(id == states.c.id)
    return await database.fetch_one(query=query)


async def get_by_name(name: str):
    query = states.select().where(name == states.c.name)
    return await database.fetch_one(query=query)


async def get_all():
    query = states.select()
    return await database.fetch_all(query=query)
