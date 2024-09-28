from sqlalchemy.orm import Session
from datetime import datetime
from .model import UserEnrollment
from .schema import EnrollmentCreate, EnrollmentUpdate
from datetime import timezone


def create_user_enrollment(
    db: Session,
    enrollment: EnrollmentCreate,
    can_commit: bool = False,
) -> UserEnrollment:
    user_enrollment = UserEnrollment(
         user_id=enrollment.user_id,
        promotion_id=enrollment.promotion_id,
        level_id=enrollment.level_id,
        time_slot_id=enrollment.time_slot_id,
        end_date=None,
        status='active',
    )
    db.add(user_enrollment)
    if can_commit:
        db.commit()
        db.refresh(user_enrollment)

    return user_enrollment


def find_existing_user_enrollment(db: Session, user_id: str, promotion_id: str):
    return (
        db.query(UserEnrollment)
        .filter(
            UserEnrollment.user_id == user_id,
            UserEnrollment.promotion_id == promotion_id,
        )
        .first()
    )

def update_user_enrollment(db: Session, enrollment_id: str, enrollment: EnrollmentUpdate):
    db.query(UserEnrollment).filter(UserEnrollment.id == enrollment_id).update(enrollment.model_dump())
    db.commit()
    return db.query(UserEnrollment).filter(UserEnrollment.id == enrollment_id).first()