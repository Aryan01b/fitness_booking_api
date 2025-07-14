from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.schemas.booking_schema import BookingRequest, BookingResponse
from app.services.booking_service import create_booking, get_bookings_by_email
from app.db.database import SessionLocal

router = APIRouter(prefix="/bookings", tags=["Bookings"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/book", response_model=BookingResponse)
def book_class(booking_request: BookingRequest, db: Session = Depends(get_db)):
    booking = create_booking(db, booking_request)
    return booking

@router.get("/", response_model=List[BookingResponse])
def read_bookings(email: str = Query(..., description="Client email to filter bookings"), db: Session = Depends(get_db)):
    bookings = get_bookings_by_email(db, email)
    return bookings
