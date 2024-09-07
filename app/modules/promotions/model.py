from sqlalchemy import Column, Date, Float, ForeignKey, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid
from datetime import datetime, timezone


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    training_type_id = Column(
        UUID(as_uuid=True), ForeignKey("training_types.id"), nullable=False
    )
    name = Column(String, nullable=False)
    price_per_month = Column(Float, nullable=False)
    promotion_start_date = Column(Date, nullable=False)
    promotion_end_date = Column(Date, nullable=False)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
