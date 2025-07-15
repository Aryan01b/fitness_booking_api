from pydantic import BaseModel
from datetime import datetime

class FitnessClassBase(BaseModel):
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

class FitnessClassResponse(FitnessClassBase):
    id: int  # class_id

    class Config:
        from_attributes = True  # Enables reading ORM objects directly in Pydantic v2
