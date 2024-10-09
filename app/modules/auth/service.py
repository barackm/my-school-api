import random
from datetime import datetime, timedelta
from ..email_service.service import send_email
from app.core.config import settings
from ..users.service import create_user, get_user_by_email_or_phone_number
from .schema import RegisterRequest, OTPVerifyRequest
from fastapi import BackgroundTasks, HTTPException


def generate_otp():
    """Generate a 6-digit OTP"""
    return random.randint(100000, 999999)


def register_user(db, user_data: RegisterRequest, background_tasks: BackgroundTasks):
    expiration_minutes = settings.OTP_EXPIRATION_MIN
    otp = generate_otp()
    otp_expiration = datetime.now() + timedelta(minutes=expiration_minutes)
    user_data = {
        "first_name": user_data.first_name,
        "last_name": user_data.last_name,
        "surname": user_data.surname,
        "phone": user_data.phone,
        "email": user_data.email,
        "otp": otp,
        "otp_expiration": otp_expiration,
        "promotion_id": None,
        "level_id": None,
        "time_slot_id": None,
        "address": None,
        "photo": None,
    }
    print(user_data)
    user = create_user(db, user_data)
    subject = "Your OTP Code"
    message = f"Your OTP code is {otp}. It will expire in {expiration_minutes} minutes."
    background_tasks.add_task(send_email, subject, user_data["email"], message)

    return user


def validate_otp(db, user_data: OTPVerifyRequest):
    user = get_user_by_email_or_phone_number(db, user_data.phone or user_data.email)
    if user.otp_expiration < datetime.now():
        raise HTTPException(status_code=400, detail="OTP has expired")
    if user.otp != user_data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    return user
