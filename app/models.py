"""
Database models for the Fitness Studio Booking API.
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class FitnessClass(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    instructor = Column(String)
    capacity = Column(Integer, nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    timezone = Column(String, nullable=False)
    version_id = Column(Integer, nullable=False, default=0)

    bookings = relationship("Booking", back_populates="fitness_class")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)
    booking_time = Column(DateTime(timezone=True), server_default=func.now())

    fitness_class = relationship("FitnessClass", back_populates="bookings")
