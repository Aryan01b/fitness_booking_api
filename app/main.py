from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import classes, bookings
from app.core.config import Settings

settings = Settings()

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="API for viewing fitness classes and booking slots"
)

# ---------------------------------------------------
# Include API Routers
# ---------------------------------------------------
app.include_router(classes.router)
app.include_router(bookings.router)

# ---------------------------------------------------
# CORS Middleware (optional, but useful for testing)
# ---------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
