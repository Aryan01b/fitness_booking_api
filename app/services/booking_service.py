from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models.class_model import FitnessClass
from app.models.booking_model import Booking
from app.schemas.booking_schema import BookingRequest

from fastapi import HTTPException, status

def create_booking(db: Session, booking_request: BookingRequest) -> Booking:
    # Get the class
    fitness_class = db.query(FitnessClass).filter(FitnessClass.id == booking_request.class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")

    # Check if slots are available
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No slots available for this class")

    # Decrement slot count
    fitness_class.available_slots -= 1
    db.add(fitness_class)

    # Create booking
    booking = Booking(
        class_id=booking_request.class_id,
        client_name=booking_request.client_name,
        client_email=booking_request.client_email,
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

def get_bookings_by_email(db: Session, email: str):
    return db.query(Booking).filter(Booking.client_email == email).all()
