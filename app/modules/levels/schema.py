from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class LevelBase(BaseModel):
    level_name: str
    level_duration: int
    training_type_id: UUID


class LevelCreate(LevelBase):
    pass


class LevelResponse(LevelBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
