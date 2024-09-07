from fastapi import FastAPI
from app.modules.students.route import router as student_router
from sqlalchemy.orm import registry
from app.modules.levels.route import router as level_router
from app.modules.promotions.route import router as promotion_router
from app.modules.training_types.route import router as training_type_router

app = FastAPI()

mapper_registry = registry()
mapper_registry.configure()

app.include_router(student_router, prefix="/students", tags=["students"])
app.include_router(level_router, prefix="/levels", tags=["levels"])
app.include_router(promotion_router, prefix="/promotions", tags=["promotions"])
app.include_router(
    training_type_router, prefix="/training_types", tags=["training_types"]
)


@app.get("/")
def read_root() -> dict:
    return {"message": "FastAPI with SQLAlchemy and Supabase"}
