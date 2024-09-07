from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime, timezone


class Student(Base):
    __tablename__ = "students"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    email = Column(String, nullable=True, unique=True)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=True)
    photo = Column(String, nullable=True, default="default_photo.jpg")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    promotions = relationship(
        "Promotion",
        secondary="student_enrollments",
        back_populates="students",
        overlaps="enrollments",
    )
    enrollments = relationship(
        "StudentEnrollment", back_populates="student", overlaps="promotions"
    )
