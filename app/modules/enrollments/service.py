from sqlalchemy.orm import Session
from datetime import datetime
from .model import StudentEnrollment


def create_student_enrollment(
    db: Session,
    student_id: int,
    promotion_id: int,
    level_id: int,
) -> StudentEnrollment:
    student_enrollment = StudentEnrollment(
        student_id=student_id,
        promotion_id=promotion_id,
        level_id=level_id,
        enrollment_date=datetime.now(),
        end_date=None,
    )
    db.add(student_enrollment)

    return student_enrollment
