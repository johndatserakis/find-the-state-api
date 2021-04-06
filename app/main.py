from routes import state, ping
from db.db import database, engine, metadata
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

metadata.create_all(engine)

app = FastAPI()

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

app.include_router(ping.router, prefix=f"{prefix}", tags=["health"])
app.include_router(state.router, prefix=f"{prefix}/states", tags=["states"])
