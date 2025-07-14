from fastapi import APIRouter, HTTPException
from app.models.booking_model import Booking
from datetime import datetime

router = APIRouter()

# In-memory bookings storage
bookings_db = []

@router.post("/book")
def book_class(class_id: int, client_name: str, client_email: str):
    # Placeholder: Check slots & book logic to be added later
    booking = Booking(
        id=len(bookings_db)+1,
        class_id=class_id,
        client_name=client_name,
        client_email=client_email,
        booking_time=datetime.utcnow()
    )
    bookings_db.append(booking)
    return {"message": "Booking successful!", "booking": booking}

@router.get("/bookings")
def get_bookings(client_email: str):
    client_bookings = [b for b in bookings_db if b.client_email == client_email]
    return client_bookings
