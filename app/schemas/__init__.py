"""Pydantic schemas for the Fitness Studio Booking API.

This package contains all Pydantic models that define the request/response
schemas for the API endpoints, providing data validation and serialization.

Schemas:
    class_schema: Schemas for fitness class operations
    booking_schema: Schemas for booking operations
"""

# Import all schema modules to ensure they're registered
from . import class_schema, booking_schema

# Re-export commonly used schemas for easier imports
from .class_schema import FitnessClassResponse
from .booking_schema import BookingRequest, BookingResponse

__all__ = [
    "FitnessClassResponse",
    "BookingRequest",
    "BookingResponse"
]
