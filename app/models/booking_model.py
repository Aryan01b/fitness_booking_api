"""Database models for class bookings.

This module defines the SQLAlchemy models for handling class bookings in the fitness booking system.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

from .class_model import Base

class Booking(Base):
    """Represents a user's booking for a fitness class.
    
    Attributes:
        id: Unique identifier for the booking (primary key).
        class_id: Reference to the booked fitness class (foreign key).
        client_name: Name of the person making the booking.
        client_email: Email address of the person making the booking (indexed for faster lookups).
    """
    __tablename__ = "bookings"

    id: int = Column(Integer, primary_key=True, index=True)
    class_id: int = Column(Integer, ForeignKey("classes.id"), nullable=False)
    client_name: str = Column(String, nullable=False)
    client_email: str = Column(String, nullable=False, index=True)
