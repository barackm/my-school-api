from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.modules.students.schema import StudentResponse, StudentCreate
from app.modules.students.service import get_students, create_student
from app.db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[StudentResponse])
def list_students(db: Session = Depends(get_db)):
    students = get_students(db=db)
    return students


@router.post("/", response_model=StudentResponse)
def create_new_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    training_type_id: str = None,
    level_id: str = None,
):
    return create_student(db, student, training_type_id, level_id)
