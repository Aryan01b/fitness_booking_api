"""Timezone conversion utilities for the fitness booking system.

This module provides functions to handle timezone conversions, particularly for
converting between the server's default timezone (IST) and other timezones.
"""
from datetime import datetime
from typing import Optional

import pytz
from app.core.config import Settings

# Load application settings
settings = Settings()

def convert_ist_to_timezone(ist_dt: datetime, tz_name: str) -> datetime:
    """Convert a datetime from IST to the specified timezone.
    
    Args:
        ist_dt: A datetime object representing a time in IST. Note that this should be
               a naive datetime (no timezone info) that represents a time in IST.
        tz_name: The target timezone name (e.g., 'America/New_York', 'Europe/London').
                 Must be a valid IANA timezone name.
    
    Returns:
        A timezone-aware datetime object in the target timezone.
    
    Raises:
        pytz.exceptions.UnknownTimeZoneError: If the provided timezone name is invalid.
        ValueError: If the input datetime is timezone-aware (should be naive).
        
    Example:
        >>> dt = datetime(2023, 1, 1, 10, 0)  # 10:00 AM IST
        >>> convert_ist_to_timezone(dt, 'America/New_York')
        datetime.datetime(2023, 1, 1, 0, 30, tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>)
    """
    if ist_dt.tzinfo is not None:
        raise ValueError("Input datetime should be naive (no timezone info)")
        
    # Get timezone objects
    ist = pytz.timezone(settings.TZ_DEFAULT)
    target = pytz.timezone(tz_name)
    
    # Localize the naive datetime to IST, then convert to target timezone
    ist_localized = ist.localize(ist_dt)
    return ist_localized.astimezone(target)
