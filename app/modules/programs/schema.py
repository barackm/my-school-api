from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List, Optional
from app.modules.levels.schema import LevelResponse
from app.modules.promotions.schema import PromotionResponse
from app.modules.time_slots.schema import TimeSlotResponse


class ProgramBase(BaseModel):
    name: str


class ProgramCreate(ProgramBase):
    pass


class ProgramResponse(ProgramBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    levels: Optional[List[LevelResponse]] = []
    promotions: Optional[List[PromotionResponse]] = []
    time_slots: Optional[List[TimeSlotResponse]] = []

    class Config:
        from_attributes = True


class ProgramsResponse(BaseModel):
    total: int
    data: List[ProgramResponse]

    class Config:
        from_attributes = True
