from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload, selectinload
from .model import TrainingType


def get_training_types(db: Session):
    return (
        db.query(TrainingType)
        .options(
            selectinload(TrainingType.levels), selectinload(TrainingType.promotions)
        )
        .all()
    )


def find_training_type_by_id(db: Session, training_type_id: str):
    training_type = (
        db.query(TrainingType)
        .filter(TrainingType.id == training_type_id)
        .options(joinedload(TrainingType.levels), joinedload(TrainingType.promotions))
        .first()
    )
    return training_type
