from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.db.database import get_db
from sqlalchemy.orm import Session
from .service import (
    get_promotion_by_id,
    get_promotions,
    get_promotion_by_program_id,
    get_promotion_by_name,
    create_promotion,
    update_promotion,
)
from ..programs.service import find_program_by_id
from .schema import PromotionResponse, PromotionCreate
from .model import Promotion
import uuid

router = APIRouter()


@router.get("/", response_model=List[PromotionResponse])
def list_promotions(db: Session = Depends(get_db)):
    return get_promotions(db)


@router.get("/{promotion_id}", response_model=PromotionResponse)
def get_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = get_promotion_by_id(db, promotion_id)
    if promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion


@router.get("/program/{program_id}", response_model=List[PromotionResponse])
def get_by_program_id(program_id: str, db: Session = Depends(get_db)):
    training_type = find_program_by_id(db, program_id)
    if training_type is None:
        raise HTTPException(status_code=404, detail="Program not found")

    promotions = get_promotion_by_program_id(db, program_id)
    return promotions


@router.post("/", response_model=PromotionCreate)
def create(promotion: PromotionCreate, db: Session = Depends(get_db)):
    program = find_program_by_id(db, promotion.program_id)

    if program is None:
        raise HTTPException(status_code=404, detail="Program not found")

    existing_promotion = get_promotion_by_name(db, promotion.name)
    if existing_promotion is not None:
        raise HTTPException(
            status_code=400,
            detail="Promotion name already exists for this program",
        )
    return create_promotion(db, promotion)


@router.put("/{promotion_id}", response_model=PromotionResponse)
def update(
    promotion_id: str, promotion: PromotionCreate, db: Session = Depends(get_db)
):
    existing_promotion = get_promotion_by_id(db, promotion_id)
    if existing_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")

    existing_promotion_with_name = get_promotion_by_name(db, promotion.name)
    if (
        existing_promotion_with_name is not None
        and existing_promotion_with_name.id != uuid.UUID(promotion_id)
    ):
        raise HTTPException(
            status_code=400,
            detail="Promotion name already exists for this program type",
        )

    return update_promotion(db, promotion_id, promotion)
