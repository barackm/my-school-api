from sqlalchemy import Column, Time, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime


class TimeSlot(Base):
    __tablename__ = "time_slots"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("training_types.id", ondelete="CASCADE"),
        nullable=False,
    )
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    )

    training_type = relationship("TrainingType", back_populates="time_slots")
    enrollments = relationship("StudentEnrollment", back_populates="time_slot")
