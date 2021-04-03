from sqlalchemy.orm import Session

from . import models, schemas


def get_state(db: Session, state_id: int):
    return db.query(models.State).filter(models.State.id == state_id).first()


def get_state_by_name(db: Session, name: str):
    return db.query(models.State).filter(models.State.name == name).first()


def get_states(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.State).offset(skip).limit(limit).all()


def create_state(db: Session, state: schemas.StateCreate):
    db_state = models.State(
        name=state.name,
        summary=state.summary,
        link=state.link,
        image=state.image,
    )
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state
