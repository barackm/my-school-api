from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime, timezone


class Level(Base):
    __tablename__ = "levels"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_type_id = Column(
        UUID(as_uuid=True), ForeignKey("training_types.id"), nullable=False
    )
    level_name = Column(String, nullable=False)
    level_duration = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    training_type = relationship("TrainingType", back_populates="levels")
