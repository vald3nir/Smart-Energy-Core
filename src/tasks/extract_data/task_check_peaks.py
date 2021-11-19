import src.utils.utils_csv as utils_csv
import src.utils.utils_io as utils_io

from src.tasks import get_path_time_series

CUTTING_POWER = 10000


def normalize_data_sets_peaks(user_name):
    for doc in utils_io.list_all_files(get_path_time_series(user_name)):
        data, peaks = utils_csv.split_data_frame_by_value(doc, 'power', CUTTING_POWER)
        if len(peaks) > 0:
            max_value = data['power'].max()
            utils_csv.normalize_data_frame_column(doc, 'power', max_value)
            print(doc, f"{len(peaks)} peaks normalized")


def remove_data_sets_peaks(user_name):
    for doc in utils_io.list_all_files(get_path_time_series(user_name)):
        data, peaks = utils_csv.split_data_frame_by_value(doc, 'power', CUTTING_POWER)
        if len(peaks) > 0:
            utils_csv.create_file_csv(doc, data)
            print(doc, f"{len(peaks)} peaks removed")
