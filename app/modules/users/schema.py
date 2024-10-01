from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from app.modules.enrollments.schema import EnrollmentResponse


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    surname: Optional[str] = None
    email: Optional[str] = None
    phone: str
    photo: Optional[str] = None
    address: Optional[str] = None
    enrollments: Optional[List[EnrollmentResponse]] = []
    otp: Optional[str] = (None,)
    otp_expiration: Optional[str] = (None,)

    promotion_id: Optional[str] = None
    level_id: Optional[str] = None
    time_slot_id: Optional[str] = None


class UserResponse(UserCreate):
    id: UUID
    status: Optional[str] = "active"

    class Config:
        from_attributes = True


class UsersResponse(BaseModel):
    total: int
    data: List[UserResponse]

    class Config:
        from_attributes = True
