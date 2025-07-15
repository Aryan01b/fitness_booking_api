"""API Version 1.0

This module contains all API endpoints for version 1.0 of the Fitness Studio Booking API.

Endpoints are organized by resource type and include:
- Classes management
- Bookings management
"""

from fastapi import APIRouter
from app.api.v1 import classes, bookings

# Create the API router for version 1
api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(classes.router, prefix="/classes", tags=["classes"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["bookings"])

__all__ = ["api_router"]
