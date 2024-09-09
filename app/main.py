from fastapi import FastAPI
from app.modules.students.route import router as student_router
from sqlalchemy.orm import registry
from app.modules.levels.route import router as level_router
from app.modules.promotions.route import router as promotion_router
from app.modules.programs.route import router as program_router
from app.modules.time_slots.route import router as time_slot_router
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

app.include_router(student_router, prefix="/students", tags=["students"])
app.include_router(level_router, prefix="/levels", tags=["levels"])
app.include_router(promotion_router, prefix="/promotions", tags=["promotions"])
app.include_router(program_router, prefix="/programs", tags=["programs"])
app.include_router(time_slot_router, prefix="/time_slots", tags=["time_slots"])


@app.get("/")
def read_root() -> dict:
    return {"message": "FastAPI with SQLAlchemy and Supabase"}
