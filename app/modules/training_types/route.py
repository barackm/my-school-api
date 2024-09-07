from fastapi import APIRouter, Depends, HTTPException
from .schema import TrainingTypeResponse, TrainingTypeCreate
from typing import List
from sqlalchemy.orm import Session
from .service import (
    get_training_types,
    create_training_type,
    get_training_type_by_name,
    find_training_type_by_id,
    update_training_type,
    delete_training_type,
)
from app.db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[TrainingTypeResponse])
def all(db: Session = Depends(get_db)):
    return get_training_types(db)


@router.post("/", response_model=TrainingTypeResponse)
def create(training: TrainingTypeCreate, db: Session = Depends(get_db)):
    existing_training = get_training_type_by_name(db, training.name)
    if existing_training:
        raise HTTPException(status_code=400, detail="Training name already exists")
    return create_training_type(db, training)


@router.put("/{training_type_id}", response_model=TrainingTypeResponse)
def update(
    training_type_id: str, training: TrainingTypeCreate, db: Session = Depends(get_db)
):
    training_type = find_training_type_by_id(db, training_type_id)
    if training_type is None:
        raise HTTPException(status_code=404, detail="Training type not found")

    existing_training = get_training_type_by_name(db, training.name)

    if training.name is not None and existing_training:
        raise HTTPException(status_code=400, detail="Training name already exists")

    return update_training_type(db, training_type_id, training)


@router.get("/{training_type_id}", response_model=TrainingTypeResponse)
def by_id(training_type_id: str, db: Session = Depends(get_db)):
    training_type = find_training_type_by_id(db, training_type_id)
    if training_type is None:
        raise HTTPException(status_code=404, detail="Training type not found")
    return training_type


@router.delete("/{training_type_id}", response_model=TrainingTypeResponse)
def delete(training_type_id: str, db: Session = Depends(get_db)):
    training_type = find_training_type_by_id(db, training_type_id)
    if training_type is None:
        raise HTTPException(status_code=404, detail="Training type not found")
    return delete_training_type(db, training_type_id)
