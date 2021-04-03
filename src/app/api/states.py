from typing import List

from app.api import crud
from app.api.models import StateDB, StateSchema
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.get("/{id}/", response_model=StateDB)
async def read_states(
    id: int = Path(..., gt=0),
):
    states = await crud.get(id)
    if not states:
        raise HTTPException(status_code=404, detail="State not found")
    return states


@router.get("/", response_model=List[StateDB])
async def read_all_statess():
    return await crud.get_all()
