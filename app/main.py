from routes import health, score, state
from db.db import database, engine, metadata
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.limiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

metadata.create_all(engine)

app = FastAPI(
    title="Find the State API",
    description="",
    version="0.0.1",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
app.include_router(score.router, prefix=f"{prefix}/scores", tags=["scores"])
