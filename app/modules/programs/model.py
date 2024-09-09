from sqlalchemy import Column, String, DateTime, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid


class Program(Base):
    __tablename__ = "programs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)

    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    )

    levels = relationship(
        "Level", back_populates="program", cascade="all, delete-orphan"
    )
    promotions = relationship(
        "Promotion", back_populates="program", cascade="all, delete-orphan"
    )
    time_slots = relationship(
        "TimeSlot", back_populates="program", cascade="all, delete-orphan"
    )
