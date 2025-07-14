from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.class_schema import FitnessClassResponse
from app.services.class_service import get_all_classes
from app.db.database import SessionLocal

router = APIRouter(prefix="/classes", tags=["Classes"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[FitnessClassResponse])
def read_classes(db: Session = Depends(get_db)):
    classes = get_all_classes(db)
    return classes
