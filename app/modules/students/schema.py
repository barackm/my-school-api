from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    surname: Optional[str]
    email: Optional[str]
    phone: str
    photo: Optional[str]
    address: Optional[str]

class StudentResponse(StudentCreate):
    id: UUID

    class Config:
        orm_mode = True
