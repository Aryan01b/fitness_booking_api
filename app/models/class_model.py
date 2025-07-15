"""Database models for fitness classes.

This module defines the SQLAlchemy models for the fitness class booking system.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()

class FitnessClass(Base):
    """Represents a fitness class that users can book.
    
    Attributes:
        id: Unique identifier for the class (primary key).
        name: Name of the fitness class (e.g., 'Yoga Flow', 'HIIT').
        datetime: Scheduled date and time of the class (stored in UTC).
        instructor: Name of the instructor leading the class.
        available_slots: Number of available slots for booking.
    """
    __tablename__ = "classes"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)
    datetime: datetime = Column(DateTime, nullable=False)
    instructor: str = Column(String, nullable=False)
    available_slots: int = Column(Integer, nullable=False)
