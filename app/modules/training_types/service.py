from sqlalchemy.orm import Session
from .model import TrainingType


def get_training_types(db: Session):
    return db.query(TrainingType).all()


def find_training_type_by_id(db: Session, training_type_id: str):
    training_type = (
        db.query(TrainingType).filter(TrainingType.id == training_type_id).first()
    )
    return training_type
