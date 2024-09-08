from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional
from app.modules.promotions.schema import PromotionResponse


class EnrollmentBase(BaseModel):
    student_id: UUID
    promotion_id: UUID
    level_id: UUID
    enrollment_date: datetime
    end_date: Optional[datetime] = None
    status: str = "active"


class EnrollmentCreate(EnrollmentBase):
    pass


class EnrollmentResponse(EnrollmentBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    promotion: PromotionResponse

    class Config:
        from_attributes = True
