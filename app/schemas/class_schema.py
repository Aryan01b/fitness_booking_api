from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime

class FitnessClassBase(BaseModel):
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

class FitnessClassResponse(FitnessClassBase):
    id: int  # class_id

    model_config = ConfigDict(from_attributes=True)  # Pydantic v2+ compatibility
