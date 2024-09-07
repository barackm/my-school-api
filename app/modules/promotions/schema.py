from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime


class PromotionBase(BaseModel):
    training_type_id: UUID
    price_per_month: float
    promotion_start_date: date
    promotion_end_date: date


class PromotionCreate(PromotionBase):
    pass


class PromotionResponse(PromotionBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
