from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, DataError
from .model import Level
from ..programs.service import find_program_by_id


def get_levels(db: Session):
    return db.query(Level).all()


def get_level_by_id(db: Session, level_id: str):
    try:
        return db.query(Level).filter(Level.id == level_id).first()
    except (SQLAlchemyError, DataError):
        return None


def get_levels_by_training_type_id(db: Session, program_id: str):
    training_type = find_program_by_id(db, program_id)
    if training_type is None:
        return None

    return db.query(Level).filter(Level.program_id == program_id).all()


def create_level(db: Session, level: Level):
    new_level = Level(
        name=level.name,
        program_id=level.program_id,
        duration=level.duration,
    )
    db.add(new_level)
    db.commit()
    db.refresh(new_level)
    return new_level


def update_level(db: Session, level_id: str, level: Level):
    existing_level = get_level_by_id(db, level_id)
    if existing_level is None:
        return None

    existing_level.name = level.name
    existing_level.duration = level.duration

    db.commit()
    db.refresh(existing_level)
    return existing_level


def delete_level(db: Session, level_id: str):
    existing_level = get_level_by_id(db, level_id)
    if existing_level is None:
        return None

    db.delete(existing_level)
    db.commit()
    return existing_level


def check_level_name_exists(db: Session, program_id: str, name: str):
    existing_level = (
        db.query(Level)
        .filter(Level.program_id == program_id)
        .filter(Level.name.ilike(name))
        .first()
    )

    return existing_level
