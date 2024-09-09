from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.exc import DataError
from .schema import ProgramCreate
from .model import Program


def get_training_types(db: Session):
    training_types = (
        db.query(Program)
        .options(selectinload(Program.levels), selectinload(Program.promotions))
        .all()
    )
    total = db.query(Program).count()
    return {"total": total, "data": training_types}


def find_program_by_id(db: Session, program_id: str):
    try:
        training_type = (
            db.query(Program)
            .filter(Program.id == program_id)
            .options(joinedload(Program.levels), joinedload(Program.promotions))
            .first()
        )
        return training_type
    except DataError:
        return None


def create_training_type(db: Session, program: ProgramCreate):
    new_training_type = Program(name=program.name)
    db.add(new_training_type)
    db.commit()
    db.refresh(new_training_type)
    return new_training_type


def get_training_type_by_name(db: Session, name: str):
    program = db.query(Program).filter(Program.name.ilike(name)).first()
    if program is None:
        return None
    training_type = find_program_by_id(db, program.id)
    return training_type


def update_training_type(db: Session, program_id: str, program: ProgramCreate):
    training_type = find_program_by_id(db, program_id)
    if training_type is None:
        return None
    training_type.name = program.name
    db.commit()
    db.refresh(training_type)
    return training_type


def delete_training_type(db: Session, program_id: str):
    training_type = find_program_by_id(db, program_id)
    if training_type is None:
        return None
    db.delete(training_type)
    db.commit()
    return training_type
