from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.db.database import get_db
from sqlalchemy.orm import Session
from .service import (
    get_promotion_by_id,
    get_promotions,
    get_promotion_by_training_type_id,
)
from ..training_types.service import find_training_type_by_id
from .schema import PromotionResponse

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


@router.get("/training/{training_type_id}", response_model=List[PromotionResponse])
def get_promotion_by_training_type(
    training_type_id: str, db: Session = Depends(get_db)
):
    training_type = find_training_type_by_id(db, training_type_id)
    if training_type is None:
        raise HTTPException(status_code=404, detail="Training type not found")

    promotions = get_promotion_by_training_type_id(db, training_type_id)
    return promotions
