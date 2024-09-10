from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.exc import DataError
from .schema import TimeSlotCreate, TimeSlotResponse, TimeSlotUpdate

from .model import TimeSlot


def get_time_slots(db: Session):
    time_slots = db.query(TimeSlot).all()
    return time_slots


def create_time_slot(db: Session, time_slot: TimeSlotCreate):
    new_time_slot = TimeSlot(
        start_time=time_slot.start_time,
        end_time=time_slot.end_time,
        program_id=time_slot.program_id,
    )
    db.add(new_time_slot)
    db.commit()
    db.refresh(new_time_slot)
    return new_time_slot


def update_time_slot(db: Session, time_slot_id: str, time_slot: TimeSlotUpdate):
    existing_time_slot = db.query(TimeSlot).filter(TimeSlot.id == time_slot_id).first()
    if existing_time_slot is None:
        return None

    existing_time_slot.start_time = time_slot.start_time
    existing_time_slot.end_time = time_slot.end_time

    db.commit()
    db.refresh(existing_time_slot)
    return existing_time_slot


def get_time_slot_by_time(db: Session, start_time: str, end_time: str, program_id: str):
    try:
        time_slot = (
            db.query(TimeSlot)
            .filter(TimeSlot.start_time == start_time)
            .filter(TimeSlot.end_time == end_time)
            .filter(TimeSlot.program_id == program_id)
            .first()
        )
        return time_slot
    except DataError:
        return None


def get_time_slot_by_id(db: Session, time_slot_id: str):
    time_slot = db.query(TimeSlot).filter(TimeSlot.id == time_slot_id).first()
    return time_slot
