from sqlalchemy.orm import Session
from .model import Level
from ..training_types.service import find_training_type_by_id


def get_levels(db: Session):
    return db.query(Level).all()


def get_level_by_id(db: Session, level_id: str):
    return db.query(Level).filter(Level.id == level_id).first()


def get_levels_by_training_type_id(db: Session, training_type_id: str):
    training_type = find_training_type_by_id(db, training_type_id)
    if training_type is None:
        return None

    return db.query(Level).filter(Level.training_type_id == training_type_id).all()
