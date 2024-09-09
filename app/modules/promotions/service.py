from sqlalchemy.orm import Session
from .model import Promotion


def get_promotions(db: Session):
    return db.query(Promotion).all()


def get_promotion_by_id(db: Session, promotion_id: str):
    return db.query(Promotion).filter(Promotion.id == promotion_id).first()


def get_promotion_by_training_type_id(db: Session, program_id: str):
    return db.query(Promotion).filter(Promotion.program_id == program_id).all()
