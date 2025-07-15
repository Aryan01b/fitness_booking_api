from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FitnessClass(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)  # class_id
    name = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)  # UTC or IST, will handle timezone later
    instructor = Column(String, nullable=False)
    available_slots = Column(Integer, nullable=False)
