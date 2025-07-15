from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingResponse(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    model_config = ConfigDict(from_attributes=True)  # Pydantic v2+ compatibility
