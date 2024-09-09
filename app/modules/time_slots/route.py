from fastapi import APIRouter, Depends, HTTPException
from .schema import TimeSlotCreate, TimeSlotResponse, TimeSlotUpdate
from typing import List
from sqlalchemy.orm import Session
from .service import (
    create_time_slot,
    get_time_slots,
    update_time_slot,
    get_time_slot_by_time,
)
from ..programs.service import find_program_by_id

from app.db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[TimeSlotResponse])
def all(db: Session = Depends(get_db)):
    return get_time_slots(db)


@router.post("/", response_model=TimeSlotResponse)
def create(time_slot: TimeSlotCreate, db: Session = Depends(get_db)):
    training_type = find_program_by_id(db, time_slot.program_id)
    if training_type is None:
        raise HTTPException(status_code=404, detail="Program not found")

    existing_time_slot = get_time_slot_by_time(
        db, time_slot.start_time, time_slot.end_time, time_slot.program_id
    )
    if existing_time_slot:
        raise HTTPException(status_code=400, detail="Time slot already exists")

    return create_time_slot(db, time_slot)


@router.put("/{time_slot_id}", response_model=TimeSlotResponse)
def update(time_slot_id: str, time_slot: TimeSlotUpdate, db: Session = Depends(get_db)):
    existing_time_slot = update_time_slot(db, time_slot_id, time_slot)
    if existing_time_slot is None:
        raise HTTPException(status_code=404, detail="Time slot not found")
    return existing_time_slot
