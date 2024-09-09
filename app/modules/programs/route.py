from fastapi import APIRouter, Depends, HTTPException
from .schema import ProgramResponse, ProgramCreate, ProgramsResponse
from typing import List
from sqlalchemy.orm import Session
from .service import (
    get_training_types,
    create_training_type,
    get_training_type_by_name,
    find_program_by_id,
    update_training_type,
    delete_training_type,
)
from app.db.database import get_db

router = APIRouter()


@router.get("/", response_model=ProgramsResponse)
def all(db: Session = Depends(get_db)):
    return get_training_types(db)


@router.post("/", response_model=ProgramResponse)
def create(program: ProgramCreate, db: Session = Depends(get_db)):
    existing_training = get_training_type_by_name(db, program.name)
    if existing_training:
        raise HTTPException(status_code=400, detail="Training name already exists")
    return create_training_type(db, program)


@router.put("/{program_id}", response_model=ProgramResponse)
def update(program_id: str, program: ProgramCreate, db: Session = Depends(get_db)):
    training_type = find_program_by_id(db, program_id)
    if training_type is None:
        raise HTTPException(status_code=404, detail="Program not found")

    existing_training = get_training_type_by_name(db, program.name)

    if program.name is not None and existing_training:
        raise HTTPException(status_code=400, detail="Training name already exists")

    return update_training_type(db, program_id, program)


@router.get("/{program_id}", response_model=ProgramResponse)
def by_id(program_id: str, db: Session = Depends(get_db)):
    training_type = find_program_by_id(db, program_id)
    if training_type is None:
        raise HTTPException(status_code=404, detail="Program not found")
    return training_type


@router.delete("/{program_id}", response_model=ProgramResponse)
def delete(program_id: str, db: Session = Depends(get_db)):
    training_type = find_program_by_id(db, program_id)
    if training_type is None:
        raise HTTPException(status_code=404, detail="Program not found")
    return delete_training_type(db, program_id)
