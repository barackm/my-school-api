from sqlalchemy import Column, Date, Numeric, ForeignKey, DateTime, String, text
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
from sqlalchemy.orm import relationship
import uuid


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("training_types.id", ondelete="CASCADE"),
        nullable=False,
    )
    name = Column(String(255), nullable=False)
    price_per_month = Column(Numeric(10, 2), nullable=False)
    promotion_start_date = Column(Date, nullable=False)
    promotion_end_date = Column(Date, nullable=False)

    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
    )

    training_type = relationship("TrainingType", back_populates="promotions")
    enrollments = relationship(
        "StudentEnrollment", back_populates="promotion", overlaps="promotions,students"
    )
    students = relationship(
        "Student",
        secondary="student_enrollments",
        back_populates="promotions",
        overlaps="enrollments",
    )
