from fastapi import HTTPException
from sqlalchemy.orm import Session
from .model import User
from .schema import UserCreate
from ..levels.service import get_level_by_id
from ..promotions.service import get_promotion_by_id
from ..enrollments.service import create_user_enrollment
from ..time_slots.service import get_time_slot_by_id


def get_users(db: Session):
    users = db.query(User).all()
    total = db.query(User).count()
    return {"total": total, "data": users}


def create_user(
    db: Session,
    user: UserCreate,
    promotion_id: str = None,
    level_id: str = None,
    time_slot_id: str = None,
):

    try:
        user_exists = get_user_by_email(db, user.email)
        if user_exists:
            raise HTTPException(
                status_code=400, detail="User with this email already exists"
            )

        new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            surname=user.surname,
            email=user.email,
            phone=user.phone,
            address=user.address,
            photo=user.photo,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        if promotion_id and level_id:
            promotion = get_promotion_by_id(db, promotion_id)
            if not promotion:
                raise HTTPException(
                    status_code=404,
                    detail=f"Promotion with id {promotion_id} not found",
                )

            level = get_level_by_id(db, level_id)
            if not level:
                raise HTTPException(
                    status_code=404, detail=f"Level with id {level_id} not found"
                )

            if level.program_id != promotion.program_id:
                raise HTTPException(
                    status_code=400,
                    detail=f"Level and promotion do not belong to the same program",
                )

            time_slot = None
            if time_slot_id:
                time_slot = get_time_slot_by_id(db, time_slot_id)
                if not time_slot:
                    raise HTTPException(
                        status_code=404,
                        detail=f"Time slot with id {time_slot_id} not found",
                    )
                if time_slot.program_id != promotion.program_id:
                    raise HTTPException(
                        status_code=400,
                        detail="Time slot does not belong to the same program as the promotion",
                    )

            enrollment = create_user_enrollment(
                db=db,
                user_id=new_user.id,
                promotion_id=promotion_id,
                level_id=level_id,
                time_slot_id=(time_slot_id if time_slot else None),
            )
            db.add(enrollment)
            db.commit()

        return new_user

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
