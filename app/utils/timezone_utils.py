from datetime import datetime
import pytz

def convert_ist_to_timezone(ist_dt: datetime, tz_name: str) -> datetime:
    """
    Convert an IST datetime to any other timezone.
    """
    ist = pytz.timezone("Asia/Kolkata")
    target = pytz.timezone(tz_name)
    ist_localized = ist.localize(ist_dt)
    return ist_localized.astimezone(target)
