from typing import List

from app.routes import ping

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/states/", response_model=schemas.State)
def create_state(state: schemas.StateCreate, db: Session = Depends(get_db)):
    db_state = crud.get_state_by_name(db, name=state.name)
    if db_state:
        raise HTTPException(status_code=400, detail="Name already used")
    return crud.create_state(db=db, state=state)


@app.get("/states/", response_model=List[schemas.State])
def read_states(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    states = crud.get_states(db, skip=skip, limit=limit)
    return states


@app.get("/states/{state_id}", response_model=schemas.State)
def read_state(state_id: int, db: Session = Depends(get_db)):
    db_state = crud.get_state(db, state_id=state_id)
    if db_state is None:
        raise HTTPException(status_code=404, detail="State not found")
    return db_state


app.include_router(ping.router, tags=["general"])
