import random
from datetime import datetime, timedelta
from ..email_service.service import send_email
from app.core.config import settings
from ..users.service import create_user
from ..users.schema import UserCreate

# from ..users.service import get_user_by_email_or_phone_number

# from app.modules.email_service.service import send_email
# from app.modules.whatsapp_service.service import send_whatsapp_message


def generate_otp():
    """Generate a 6-digit OTP"""
    return random.randint(100000, 999999)


def register_user(db, user_data: UserCreate):
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
    }
    user = create_user(db, user_data)
    subject = "Your OTP Code"
    message = f"Your OTP code is {otp}. It will expire in {expiration_minutes} minutes."
    send_email(subject, user_data.email, message)
    return user
