"""
Configuration settings for the Fitness Studio Booking API.
Loads environment variables and provides application settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./fitness.db")
API_KEY = os.getenv("API_KEY")
