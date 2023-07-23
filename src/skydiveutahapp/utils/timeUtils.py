from datetime import datetime

from pytz import timezone
import pytz



def get_current_date_yyyymmdd():
    # Get the current date and time
    current_datetime = datetime.now()
    # Format the date as YYYYMMDD
    formatted_date = current_datetime.strftime('%Y%m%d')
    return formatted_date



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


def convert_to_mst_from_ISO_8601(iso_string):
    try:
        # Parse the ISO 8601 formatted string to a datetime object
        dt = datetime.fromisoformat(iso_string)
        # Get the Mountain Time (US/Mountain) timezone
        mst = pytz.timezone('US/Mountain')
        mst_time = dt.astimezone(mst).strftime('%I:%M%p')
        return mst_time
        # 2023-07-21T14:00:00-06:00
        # 02:00PM

    except ValueError:
        raise ValueError("Invalid ISO 8601 formatted datetime string.")
