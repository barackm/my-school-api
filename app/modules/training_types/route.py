from fastapi import APIRouter, Depends, HTTPException
from .schema import TrainingTypeResponse, TrainingTypeCreate
from typing import List
from sqlalchemy.orm import Session
from .service import get_training_types, create_training_type, get_training_type_by_name
from app.db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[TrainingTypeResponse])
def all(db: Session = Depends(get_db)):
    return get_training_types(db)


@router.post("/", response_model=TrainingTypeResponse)
def create(training: TrainingTypeCreate, db: Session = Depends(get_db)):
    existing_training = get_training_type_by_name(db, training.name)
    if existing_training:
        raise HTTPException(status_code=400, detail="Training type already exists")
    return create_training_type(db, training)
