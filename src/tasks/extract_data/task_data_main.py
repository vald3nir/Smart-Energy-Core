import src.utils.utils_io as utils_io
from src.tasks import USERS_FOLDER
from src.tasks.extract_data.task_database_backup import backup_collection
from src.tasks.extract_data.task_reduce_time_series import reduce_time_series
from src.tasks.extract_data.task_validate_datasets_header import check_time_series_header

if __name__ == '__main__':

    print("Step 1: checking if the time series has header")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        check_time_series_header(user_name)

    print("Step 2: reducing if the time series files")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        reduce_time_series(user_name)

    print("Step 3: database backup")
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        backup_collection(user_name)

    print("Finish")
