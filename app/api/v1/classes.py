from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.class_schema import FitnessClassResponse
from app.services.class_service import get_all_classes
from app.db.database import SessionLocal

router = APIRouter(prefix="/api/v1", tags=["Classes"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import Query
from app.utils.timezone_utils import convert_ist_to_timezone
from app.core.config import Settings

settings = Settings()

@router.get("/classes", response_model=List[FitnessClassResponse])
def read_classes(
    db: Session = Depends(get_db),
    display_tz: str = Query(None, description="Timezone name for display (e.g. 'UTC', 'America/New_York')")
):
    classes = get_all_classes(db)
    tz = display_tz or settings.TZ_DEFAULT
    out = []
    for c in classes:
        c_dict = c.__dict__.copy()
        if c_dict.get("datetime"):
            try:
                c_dict["datetime"] = convert_ist_to_timezone(c_dict["datetime"], tz).isoformat()
            except Exception:
                c_dict["datetime"] = c_dict["datetime"].isoformat()
        out.append(c_dict)
    return out
