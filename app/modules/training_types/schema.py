from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class TrainingTypeBase(BaseModel):
    name: str


class TrainingTypeCreate(TrainingTypeBase):
    pass


class TrainingTypeResponse(TrainingTypeBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
