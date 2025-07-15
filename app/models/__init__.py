"""Database models for the Fitness Studio Booking API.

This package contains all SQLAlchemy models that represent the application's
data structure in the database.

Models:
    FitnessClass: Represents a fitness class/session
    Booking: Represents a user's booking for a class
"""

from .class_model import FitnessClass
from .booking_model import Booking

# This ensures that SQLAlchemy can discover all models
__all__ = ["FitnessClass", "Booking"]
