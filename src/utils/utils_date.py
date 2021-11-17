from datetime import datetime
from pytz import timezone


def timestamp_to_date(timestamp):
    timestamp = timestamp / 1000
    return datetime.fromtimestamp(timestamp, tz=timezone('America/Sao_Paulo'))


def get_today_date_formatted():
    return datetime.today().strftime('%Y-%m-%d')


def get_current_month_year():
    return datetime.today().strftime('%Y-%m')


def get_current_year():
    return datetime.today().strftime('%Y')


def get_today_date_utc():
    return datetime.utcnow()
