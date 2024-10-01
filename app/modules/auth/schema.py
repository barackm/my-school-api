from pydantic import BaseModel, BaseModel, EmailStr, Field, model_validator


class OTPRequest(BaseModel):
    email: str = None
    phone_number: str = None


class OTPVerifyRequest(BaseModel):
    otp: int
    email: str = None
    phone_number: str = None


class AuthResponse(BaseModel):
    message: str
    token: str = None


class RegisterRequest(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    surname: str = None
    email: EmailStr = None
    phone: str = Field(None, min_length=10, max_length=15)
    verify_with: str

    @model_validator(mode="before")
    def check_email_or_phone(cls, values):
        email = values.get("email")
        phone = values.get("phone")
        if not email and not phone:
            raise ValueError("Either email or phone number must be provided")
        return values
