from fastapi import APIRouter, Depends
from .schema import TrainingTypeResponse
from typing import List
from sqlalchemy.orm import Session
from .service import get_training_types
from app.db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[TrainingTypeResponse])
def list_training_types(db: Session = Depends(get_db)):
    return get_training_types(db)
