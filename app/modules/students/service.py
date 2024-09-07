from fastapi import HTTPException
from sqlalchemy.orm import Session
from .model import Student
from .schema import StudentCreate
from ..levels.service import get_level_by_id
from ..promotions.service import get_promotion_by_id
from ..enrollments.service import create_student_enrollment


def get_students(db: Session):
    return db.query(Student).all()


def create_student(
    db: Session,
    student: StudentCreate,
    promotion_id: str = None,
    level_id: str = None,
):
    try:
        with db.begin():
            if promotion_id is not None:
                promotion = get_promotion_by_id(db, promotion_id)
                if not promotion:
                    raise HTTPException(status_code=404, detail="Promotion not found")

            if level_id is not None:
                level = get_level_by_id(db, level_id)
                if not level:
                    raise HTTPException(status_code=404, detail="Level not found")

            new_student = Student(
                first_name=student.first_name,
                last_name=student.last_name,
                surname=student.surname,
                email=student.email,
                phone=student.phone,
                address=student.address,
                photo=student.photo,
            )
            db.add(new_student)
            db.commit()
            db.refresh(new_student)

            if promotion_id is not None and level_id is not None:
                create_student_enrollment(
                    db=db,
                    student_id=new_student.id,
                    promotion_id=promotion_id,
                    level_id=level_id,
                )

            return new_student

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Failed to create student: {str(e)}"
        )


def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()
