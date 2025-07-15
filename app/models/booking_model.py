from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

from .class_model import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False, index=True)
