from fastapi import FastAPI
from app.modules.users.route import router as user_router
from sqlalchemy.orm import registry
from app.modules.levels.route import router as level_router
from app.modules.promotions.route import router as promotion_router
from app.modules.programs.route import router as program_router
from app.modules.time_slots.route import router as time_slot_router
from app.modules.enrollments.route import router as enrollment_router
from app.modules.auth.route import router as auth_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mapper_registry = registry()
mapper_registry.configure()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(level_router, prefix="/levels", tags=["levels"])
app.include_router(promotion_router, prefix="/promotions", tags=["promotions"])
app.include_router(program_router, prefix="/programs", tags=["programs"])
app.include_router(time_slot_router, prefix="/time-slots", tags=["time-slots"])
app.include_router(enrollment_router, prefix="/enrollments", tags=["enrollments"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/")
def read_root() -> dict:
    return {"message": "FastAPI with SQLAlchemy and Supabase"}
