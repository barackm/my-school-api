from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_models():
    from app.modules.users.model import User
    from app.modules.promotions.model import Promotion
    from app.modules.levels.model import Level
    from app.modules.time_slots.model import TimeSlot
    from app.modules.programs.model import Program
    from app.modules.enrollments.model import UserEnrollment
