from sqlalchemy.orm import Session
from datetime import datetime
from .model import UserEnrollment


def create_user_enrollment(
    db: Session,
    user_id: int,
    promotion_id: int,
    level_id: str,
    time_slot_id: str,
) -> UserEnrollment:
    user_enrollment = UserEnrollment(
        user_id=user_id,
        promotion_id=promotion_id,
        level_id=level_id,
        enrollment_date=datetime.now(),
        end_date=None,
        time_slot_id=time_slot_id,
    )
    db.add(user_enrollment)

    return user_enrollment
