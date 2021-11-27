import src.utils.utils_io as utils_io
from src.tasks import get_path_time_series, get_path_time_series_cached


def cache_time_series(_user_name):
    path_time_series = get_path_time_series(_user_name)
    path_time_series_cached = get_path_time_series_cached(_user_name)

    utils_io.create_folder_if_not_exist(path_time_series_cached)

    for doc in utils_io.list_all_files(path_time_series):
        new_path = doc.replace(path_time_series, path_time_series_cached)
        print(f"moving {doc} to {new_path}")
        utils_io.move_file(doc, new_path)
