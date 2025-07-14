from datetime import datetime
from pydantic import BaseModel

class Booking(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: str
    booking_time: datetime
