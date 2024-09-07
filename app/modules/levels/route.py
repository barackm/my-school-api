from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from .model import Level
from app.db.database import get_db
from .service import get_levels, get_level_by_id, get_levels_by_training_type_id
from .schema import LevelResponse


router = APIRouter()


@router.get("/", response_model=List[LevelResponse])
def list_levels(db: Session = Depends(get_db)):
    return get_levels(db)


@router.get("/{level_id}", response_model=LevelResponse)
def get_level(level_id: int, db: Session = Depends(get_db)):
    level = get_level_by_id(db, level_id)
    if level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    return level


@router.get("/training_type/{training_type_id}", response_model=List[LevelResponse])
def get_levels_by_training(training_type_id: str, db: Session = Depends(get_db)):
    levels = get_levels_by_training_type_id(db, training_type_id)
    if levels is None:
        raise HTTPException(status_code=404, detail="Training type not found")
    return levels
