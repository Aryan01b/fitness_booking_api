from sqlalchemy.orm import Session
from typing import List
from app.models.class_model import FitnessClass

def get_all_classes(db: Session) -> List[FitnessClass]:
    return db.query(FitnessClass).all()
