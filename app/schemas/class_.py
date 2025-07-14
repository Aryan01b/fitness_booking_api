"""
Pydantic schemas for Class model.
"""
from pydantic import BaseModel
from datetime import datetime

class FitnessClassBase(BaseModel):
    name: str
    description: str
    instructor: str
    capacity: int
    start_time: datetime
    end_time: datetime
    timezone: str

class FitnessClassCreate(FitnessClassBase):
    pass

class FitnessClassOut(FitnessClassBase):
    id: int

    class Config:
        orm_mode = True
