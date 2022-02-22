import src.utils.utils_io as utils_io
from src.tasks import USERS_FOLDER
from src.tasks.database.task_database_backup import backup_collection
from src.tasks.extract_data.task_cache_files import cache_time_series
from src.tasks.extract_data.task_check_duplicates import check_duplicates
from src.tasks.extract_data.task_check_peaks import normalize_data_sets_peaks
from src.tasks.extract_data.task_reduce_time_series import reduce_time_series
from src.tasks.extract_data.task_validate_header import check_time_series_header
from src.tasks.plot_data.task_plot_consumption_daily import plot_consumption_daily
from src.tasks.plot_data.task_plot_consumption_montly import plot_consumption_monthly
from src.tasks.plot_data.task_plot_consumption_yearly import plot_consumption_yearly
from src.tasks.plot_data.task_plot_last_consumption_days import plot_last_consumption_days
from src.tasks.plot_data.task_plot_last_consumption_months import plot_last_consumption_months


def extract_data():
    print("Step 0: move the time series to cache")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        cache_time_series(user_name)

    print("Step 1: checking if the time series has header")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        check_time_series_header(user_name)

    print("Step 2: normalizing peaks")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        normalize_data_sets_peaks(user_name)

    print("Step 3: reducing if the time series files")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        reduce_time_series(user_name)

    print("Step 4: check duplicates")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        check_duplicates(user_name)

    print("Step 5: database backup")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        backup_collection(user_name)


def plot_data():
    _user_name = "Valdenir"
    plot_consumption_daily(_user_name=_user_name, _date="2021-11-18")
    plot_consumption_monthly(_user_name=_user_name, _date="2021-10")
    plot_consumption_yearly(_user_name=_user_name, _year="2021")
    plot_last_consumption_days(_user_name=_user_name, num_days=5)
    plot_last_consumption_months(_user_name, num_months=24)


if __name__ == "__main__":
    extract_data()
    # plot_data()
