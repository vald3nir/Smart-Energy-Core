from datetime import datetime


def get_date_formatted(date_time_str):
    if len(date_time_str) == 26:
        date = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    else:
        date = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    return date.strftime("%Y-%m-%dT%H:%M:%SZ")


def get_today_date_formatted():
    return datetime.today().strftime('%Y-%m-%d')


def get_current_month_year():
    return datetime.today().strftime('%Y-%m')


def get_current_year():
    return datetime.today().strftime('%Y')


def get_today_date_utc():
    return datetime.utcnow()
