from asyncpg.exceptions import UniqueViolationError
from fastapi import APIRouter, HTTPException, Path
from schemas.score import Score, ScoreCreate, ScoreUpdate, ScoreDelete
from typing import List
import crud.score as crud
import uuid

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


@router.get("/", response_model=List[Score])
async def read_all():
    """
    Get all items
    """
    return await crud.get_all()


@router.post("/", response_model=Score, status_code=201)
async def create(payload: ScoreCreate):
    """
    Create item.
    """
    try:
        item_id = await crud.create(payload)
        new_row = await crud.get(item_id)
    except Exception:
        raise HTTPException(status_code=500, detail="Error processing request")

    return new_row


@router.put("/{id}", response_model=Score)
async def update(id: uuid.UUID, payload: ScoreUpdate):
    """
    Update item.
    """
    item = await crud.get(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    try:
        item_id = await crud.update(id, payload)
        updated_row = await crud.get(item_id)
    except Exception:
        raise HTTPException(status_code=500, detail="Error processing request")

    return updated_row


@router.delete("/{id}", response_model=ScoreDelete)
async def delete(id: uuid.UUID):
    """
    Delete item.
    """
    try:
        await crud.delete(id)
    except Exception:
        raise HTTPException(status_code=500, detail="Error processing request")

    return {"id": id}
