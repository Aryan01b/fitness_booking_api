"""Service layer for the Fitness Studio Booking API.

This package contains the business logic and data processing for the application,
separating it from the API endpoints and database models.

Services:
    class_service: Business logic for fitness class operations
    booking_service: Business logic for booking operations
"""

# Import all service modules to ensure they're registered
from . import class_service, booking_service

# Re-export commonly used service functions for easier imports
from .class_service import get_all_classes
from .booking_service import create_booking, get_bookings_by_email

__all__ = [
    "get_all_classes",
    "create_booking",
    "get_bookings_by_email"
]
