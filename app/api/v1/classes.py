from fastapi import APIRouter
from app.models.class_model import FitnessClass
from datetime import datetime

router = APIRouter()

# Mock in-memory DB for classes
classes_db = [
    FitnessClass(id=1, name="Yoga", datetime=datetime(2025, 7, 15, 10, 0), instructor="Alice", available_slots=10),
    FitnessClass(id=2, name="Zumba", datetime=datetime(2025, 7, 15, 12, 0), instructor="Bob", available_slots=15)
]

@router.get("/classes")
def get_classes():
    return classes_db
