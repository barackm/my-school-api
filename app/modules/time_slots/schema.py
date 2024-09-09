from pydantic import BaseModel
from uuid import UUID
from datetime import time, datetime


class TimeSlotBase(BaseModel):
    start_time: time
    end_time: time
    program_id: UUID


class TimeSlotCreate(TimeSlotBase):
    pass


class TimeSlotUpdate(TimeSlotBase):
    start_time: time
    end_time: time


class TimeSlotResponse(TimeSlotBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
