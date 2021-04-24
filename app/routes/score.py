from asyncpg.exceptions import UniqueViolationError
from fastapi import APIRouter, Depends, HTTPException, Path, Request
from schemas.score import Score, ScoreCreate, ScoreUpdate, ScoreDelete
from typing import List
import crud.score as crud
import uuid
from utils.env import get_settings

router = APIRouter()


@router.get("/{id}", response_model=Score)
async def read(id: uuid.UUID):
    """
    Get item by id.
    """
    item = await crud.get(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("", response_model=List[Score])
async def read_all():
    """
    Get all items
    """
    return await crud.get_all()


@router.post("", response_model=Score, status_code=201)
async def create(payload: ScoreCreate):
    """
    Create item.
    """
    if payload.token != get_settings().auth_secret:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        item_id = await crud.create(payload)
        new_row = await crud.get(item_id)
    except Exception:
        raise HTTPException(status_code=500, detail="Error processing request")

    return new_row
