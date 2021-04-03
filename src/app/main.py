from app.routes import state, ping
from app.db.db import database, engine, metadata
from fastapi import FastAPI

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router, tags=["health"])
app.include_router(state.router, prefix="/states", tags=["states"])
