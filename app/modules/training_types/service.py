from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload, selectinload
from .schema import TrainingTypeCreate
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


def create_training_type(db: Session, training: TrainingTypeCreate):
    new_training_type = TrainingType(name=training.name)
    db.add(new_training_type)
    db.commit()
    db.refresh(new_training_type)
    return new_training_type


def get_training_type_by_name(db: Session, name: str):
    return db.query(TrainingType).filter(TrainingType.name.ilike(name)).first()
