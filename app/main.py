from fastapi import FastAPI
from app.api.v1 import classes, bookings

app = FastAPI(title="Fitness Studio Booking API")

app.include_router(classes.router, tags=["Classes"])
app.include_router(bookings.router, tags=["Bookings"])
