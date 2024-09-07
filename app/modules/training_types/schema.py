from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List, Optional
from app.modules.levels.schema import LevelResponse
from app.modules.promotions.schema import PromotionResponse


class TrainingTypeBase(BaseModel):
    name: str


class TrainingTypeCreate(TrainingTypeBase):
    pass


class TrainingTypeResponse(TrainingTypeBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    levels: Optional[List[LevelResponse]] = []
    promotions: Optional[List[PromotionResponse]] = []

    class Config:
        orm_mode = True
