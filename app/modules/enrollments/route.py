from fastapi import APIRouter, Depends, HTTPException
from app.modules.enrollments.service import (
    create_user_enrollment,
    find_existing_user_enrollment,
)
from sqlalchemy.orm import Session
from .schema import EnrollmentResponse, EnrollmentCreate
from app.db.database import get_db
from sqlalchemy.exc import IntegrityError

router = APIRouter()


@router.post("/", response_model=EnrollmentResponse)
def create(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db),
):
    existing = find_existing_user_enrollment(
        db, enrollment.user_id, enrollment.promotion_id
    )
    if existing:
        raise HTTPException(
            status_code=400, detail="User already enrolled in this promotion"
        )

    try:
        return create_user_enrollment(db, enrollment, can_commit=True)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Unable to create enrollment. Please check if all referenced IDs (user, promotion, level, time_slot) are valid."
        ) from e
