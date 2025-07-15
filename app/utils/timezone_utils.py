from datetime import datetime
from app.core.config import Settings
import pytz

settings = Settings()

def convert_ist_to_timezone(ist_dt: datetime, tz_name: str) -> datetime:
    """
    Convert an IST datetime to any other timezone.
    """
    ist = pytz.timezone(settings.TZ_DEFAULT)
    target = pytz.timezone(tz_name)
    ist_localized = ist.localize(ist_dt)
    return ist_localized.astimezone(target)
