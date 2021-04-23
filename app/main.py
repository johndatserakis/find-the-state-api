from routes import state, health
from db.db import database, engine, metadata
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

metadata.create_all(engine)

app = FastAPI(
    title="Find the State API",
    description="",
    version="0.0.1",
)

# https://fastapi.tiangolo.com/tutorial/cors/?h=%20cors#use-corsmiddleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


prefix = "/api/v1"

app.include_router(health.router, prefix=f"{prefix}", tags=["health"])
app.include_router(state.router, prefix=f"{prefix}/states", tags=["states"])

# Keep user routes in its own file
from routes import user
