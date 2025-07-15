from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Fitness Studio Booking API"
    TZ_DEFAULT: str = "Asia/Kolkata"
