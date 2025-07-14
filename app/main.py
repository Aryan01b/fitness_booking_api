"""
Main application module for Omnify Fitness Studio Booking API.

This module serves as the entry point for the FastAPI application.
"""
from fastapi import FastAPI
from .database import engine, Base

# Initialize FastAPI
app = FastAPI(title="Fitness Studio Booking API")

# Create tables on startup
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Fitness Studio Booking API is running 🚀"}
