from sqlalchemy.orm import Session
from .model import Promotion
from sqlalchemy import asc


def get_promotions(db: Session):
    return db.query(Promotion).order_by(asc(Promotion.promotion_start_date)).all()


def get_promotion_by_id(db: Session, promotion_id: str):
    return db.query(Promotion).filter(Promotion.id == promotion_id).first()


def get_promotion_by_program_id(db: Session, program_id: str):
    return db.query(Promotion).filter(Promotion.program_id == program_id).all()


def get_promotion_by_name(db: Session, program_name: str):
    return db.query(Promotion).filter(Promotion.name.ilike(f"%{program_name}%")).first()


def create_promotion(db: Session, promotion: Promotion):
    new_promotion = Promotion(
        name=promotion.name,
        program_id=promotion.program_id,
        discount=promotion.discount,
        promotion_start_date=promotion.promotion_start_date,
        promotion_end_date=promotion.promotion_end_date,
        general_fee=promotion.general_fee,
        installments=promotion.installments,
    )
    db.add(new_promotion)
    db.commit()
    db.refresh(new_promotion)
    return new_promotion


def update_promotion(db: Session, promotion_id: str, promotion: Promotion):
    existing_promotion = get_promotion_by_id(db, promotion_id)
    if existing_promotion is None:
        return None

    existing_promotion.name = promotion.name
    existing_promotion.discount = promotion.discount
    existing_promotion.promotion_start_date = promotion.promotion_start_date
    existing_promotion.promotion_end_date = promotion.promotion_end_date
    existing_promotion.general_fee = promotion.general_fee
    existing_promotion.installments = promotion.installments

    db.commit()
    db.refresh(existing_promotion)
    return existing_promotion
