from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from .model import Level
from app.db.database import get_db
from ..training_types.service import (
    find_training_type_by_id,
)
from .service import (
    get_levels,
    get_level_by_id,
    get_levels_by_training_type_id,
    check_level_name_exists,
    create_level,
    update_level,
    delete_level,
)
from .schema import LevelResponse, LevelCreate


router = APIRouter()


@router.get("/", response_model=List[LevelResponse])
def list_levels(db: Session = Depends(get_db)):
    return get_levels(db)


@router.get("/{level_id}", response_model=LevelResponse)
def get_level(level_id: str, db: Session = Depends(get_db)):
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


@router.post("/", response_model=LevelResponse)
def create(level: LevelCreate, db: Session = Depends(get_db)):
    training = find_training_type_by_id(db, level.training_type_id)

    if training is None:
        raise HTTPException(status_code=404, detail="Training type not found")

    existing_level = check_level_name_exists(db, level.training_type_id, level.name)
    if existing_level:
        raise HTTPException(
            status_code=400, detail="Level name already exists for this training type"
        )

    return create_level(db, level)


@router.put("/{level_id}", response_model=LevelResponse)
def update(level_id: str, level: LevelCreate, db: Session = Depends(get_db)):
    existing_level = get_level_by_id(db, level_id)
    if existing_level is None:
        raise HTTPException(status_code=404, detail="Level not found")

    training = find_training_type_by_id(db, level.training_type_id)
    if training is None:
        raise HTTPException(status_code=404, detail="Training type not found")

    existing_level = check_level_name_exists(db, level.training_type_id, level.name)
    if existing_level:
        raise HTTPException(
            status_code=400, detail="Level name already exists for this training type"
        )

    return update_level(db, level_id, level)


@router.delete("/{level_id}", response_model=LevelResponse)
def delete(level_id: str, db: Session = Depends(get_db)):
    level = get_level_by_id(db, level_id)
    if level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    return delete_level(db, level_id)
