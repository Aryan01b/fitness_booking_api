"""
Pydantic schemas for Booking model.
"""
from pydantic import BaseModel, EmailStr
from datetime import datetime

class BookingBase(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingCreate(BookingBase):
    pass

class BookingOut(BookingBase):
    id: int
    booking_time: datetime

    class Config:
        orm_mode = True
