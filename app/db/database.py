import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pytz

from app.models.class_model import Base, FitnessClass
from app.models.booking_model import Booking  # Needed for Base metadata

# ---------------------------------------------------
# Remove the existing test.db file if it exists
# ---------------------------------------------------
db_path = './test.db'
if os.path.exists(db_path):
    os.remove(db_path)

# ---------------------------------------------------
# 1. SQLite In-Memory Engine
# ---------------------------------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# ---------------------------------------------------
# 2. Session Local
# ---------------------------------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ---------------------------------------------------
# 3. Create Tables
# ---------------------------------------------------
Base.metadata.create_all(bind=engine)

# ---------------------------------------------------
# 4. Seed Initial Class Data (Yoga, Zumba, HIIT)
# ---------------------------------------------------
def seed_data():
    db = SessionLocal()
    # Only seed if there are no classes
    if db.query(FitnessClass).first():
        db.close()
        return  # Already seeded

    from app.utils.timezone_utils import convert_ist_to_timezone
    now_naive = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    classes = [
        FitnessClass(
            name="Yoga",
            datetime=convert_ist_to_timezone(now_naive.replace(hour=7), "Asia/Kolkata"),
            instructor="Alice",
            available_slots=10,
        ),
        FitnessClass(
            name="Zumba",
            datetime=convert_ist_to_timezone(now_naive.replace(hour=9), "Asia/Kolkata"),
            instructor="Bob",
            available_slots=0,
        ),
        FitnessClass(
            name="HIIT",
            datetime=convert_ist_to_timezone(now_naive.replace(hour=18), "Asia/Kolkata"),
            instructor="Charlie",
            available_slots=12,
        ),
    ]

    db.add_all(classes)
    db.commit()
    db.close()

# ---------------------------------------------------
# 5. Run seed once when this file is imported
# ---------------------------------------------------
seed_data()
