from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.modules.students.schema import StudentResponse, StudentsResponse, StudentCreate
from app.modules.students.service import get_students, create_student
from app.db.database import get_db

router = APIRouter()


@router.get("/", response_model=StudentsResponse)
def all(db: Session = Depends(get_db)):
    students = get_students(db=db)
    return students


@router.post("/", response_model=StudentResponse)
def create_new_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    program_id: str = None,
    level_id: str = None,
):
    return create_student(db, student, program_id, level_id)
