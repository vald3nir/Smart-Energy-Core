USERS_FOLDER = "src/users/"


def get_time_series_collection_name(_user_name):
    return f"{_user_name}_TimeSeries"


def get_path_time_series(_user_name):
    return f"{USERS_FOLDER}{_user_name}/time_series"


def get_path_time_series_cached(_user_name):
    return f"{USERS_FOLDER}{_user_name}/cache"


def get_path_consumption_summary(_user_name):
    return f"{USERS_FOLDER}{_user_name}/consumption_summary.csv"
