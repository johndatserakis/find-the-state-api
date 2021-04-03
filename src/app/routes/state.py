from typing import List
import app.crud.state as crud
from app.models.state import State
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.get("/{id}/", response_model=State)
async def read_states(id: int):
    states = await crud.get_by_id(id)
    if not states:
        raise HTTPException(status_code=404, detail="State not found")
    return states


@router.get("/{name}/", response_model=State)
async def read_states(name: str):
    states = await crud.get_by_name(name)
    if not states:
        raise HTTPException(status_code=404, detail="State not found")
    return states


@router.get("/", response_model=List[State])
async def read_all_states():
    return await crud.get_all()
