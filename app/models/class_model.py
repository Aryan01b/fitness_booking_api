from datetime import datetime
from pydantic import BaseModel

class FitnessClass(BaseModel):
    id: int
    name: str
    datetime: datetime
    instructor: str
    available_slots: int
