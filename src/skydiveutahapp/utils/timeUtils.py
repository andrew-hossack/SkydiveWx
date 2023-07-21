from datetime import datetime

from pytz import timezone


def zulu_to_mst_string(time):
    
    zulu_tz = timezone('UTC')
    mst_tz = timezone('US/Mountain')

    # If time is a string, convert it to datetime
    if isinstance(time, str):
        # Use today's date and the given Zulu hour
        time = datetime.now().replace(hour=int(time), minute=0, second=0, microsecond=0)
    
    # Making the time timezone aware
    dt = zulu_tz.localize(time)

    # Converting to MST
    mst_time = dt.astimezone(mst_tz)
            
    # Returning the converted time
    return mst_time.strftime('%-I:%M%p') + " MST"

def convert_utc_to_mst(time):
    # Make dt timezone aware
    utc_tz = timezone('UTC')
    dt = utc_tz.localize(time)

    # Convert to MST
    mst_tz = timezone('US/Mountain')
    return dt.astimezone(mst_tz)


def time_diff(time):
    metar_time = convert_utc_to_mst(time)
    now_time = convert_utc_to_mst(datetime.utcnow())
    diff = now_time - metar_time

    # Get the difference in days, hours, minutes, seconds
    seconds = diff.seconds
    minutes = (seconds % 3600) // 60

    return f'{minutes} minutes ago'

def get_time_now_mst():
    utc_tz = timezone('UTC')
    now_utc = utc_tz.localize(datetime.utcnow())

    mst_tz = timezone('US/Mountain')
    now_mst = now_utc.astimezone(mst_tz)

    return now_mst.strftime('%Y-%m-%d %H:%M:%S %Z%z')

def convert_to_mst_from_ISO_8601(time_str):
    # Parse string to datetime object
    dt = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z")

    # Convert to Mountain Standard Time
    mst = timezone('MST')
    dt_mst = dt.astimezone(mst)

    # Format time in a more human-readable way
    formatted_time = dt_mst.strftime('%I:%M%p')

    return formatted_time