from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pytz

from app.models.class_model import Base, FitnessClass
from app.models.booking_model import Booking  # Needed for Base metadata

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
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)

    classes = [
        FitnessClass(
            name="Yoga",
            datetime=now.replace(hour=7, minute=0, second=0, microsecond=0),
            instructor="Alice",
            available_slots=10,
        ),
        FitnessClass(
            name="Zumba",
            datetime=now.replace(hour=9, minute=0, second=0, microsecond=0),
            instructor="Bob",
            available_slots=15,
        ),
        FitnessClass(
            name="HIIT",
            datetime=now.replace(hour=18, minute=0, second=0, microsecond=0),
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
