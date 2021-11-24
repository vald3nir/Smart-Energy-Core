# coding=utf-8
# !/usr/bin/python3

import src.utils.utils_io as utils_io
from src.tasks import USERS_FOLDER
from src.tasks.database.task_database_backup import backup_collection
from src.tasks.extract_data.task_check_peaks import normalize_data_sets_peaks
from src.tasks.extract_data.task_reduce_time_series import reduce_time_series
from src.tasks.extract_data.task_validate_header import check_time_series_header
from src.tasks.plot_data.task_plot_consumption_daily import plot_consumption_daily
from src.tasks.plot_data.task_plot_consumption_montly import plot_consumption_monthly
from src.tasks.plot_data.task_plot_consumption_yearly import plot_consumption_yearly


def calculate_energy_consumption():
    print("Step 1: checking if the time series has header")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        check_time_series_header(user_name)

    print("Step 2: normalizing peaks")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        normalize_data_sets_peaks(user_name)

    print("Step 3: reducing if the time series files")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        reduce_time_series(user_name)

    print("Step 4: database backup")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        backup_collection(user_name)


def plot_consumption():
    _user_name = "Valdenir"
    # plot_consumption_daily(_user_name=_user_name, _date="2021-11-18")
    plot_consumption_monthly(_user_name=_user_name, _date="2021-10")
    # plot_consumption_yearly(_user_name=_user_name, _year="2021")


if __name__ == '__main__':
    # calculate_energy_consumption()
    plot_consumption()
