from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class LevelBase(BaseModel):
    name: str
    duration: int
    program_id: UUID


class LevelCreate(LevelBase):
    pass


class LevelResponse(LevelBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
