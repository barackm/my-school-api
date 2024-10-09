from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.database import get_db
from .schema import RegisterRequest, OTPVerifyRequest
from .service import register_user, validate_otp


router = APIRouter()


@router.post("/register")
def register(
    user: RegisterRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    user = register_user(db, user, background_tasks)
    return user


@router.post("/verify-otp")
def verify_otp(user: OTPVerifyRequest, db: Session = Depends(get_db)):
    user = validate_otp(db, user)
    return user
