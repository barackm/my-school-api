from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime


class PromotionBase(BaseModel):
    program_id: UUID
    promotion_start_date: date
    promotion_end_date: date
    general_fee: float
    installments: float
    name: str


class PromotionCreate(PromotionBase):
    pass


class PromotionResponse(PromotionBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
