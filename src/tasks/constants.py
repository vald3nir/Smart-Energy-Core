import math

USERS_FOLDER = "../users/"

WATTS_SECONDS_TO_KILOWATT_HOURS = 2.778 * math.pow(10, -7)


def get_path_time_series(_user_name):
    return f"{USERS_FOLDER}{_user_name}/time_series"


def get_path_consumption_summary(_user_name):
    return f"{USERS_FOLDER}{_user_name}/consumption_summary"
