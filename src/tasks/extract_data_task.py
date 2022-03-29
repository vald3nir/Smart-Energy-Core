import math

import src.utils.utils_csv as utils_csv
import src.utils.utils_date as utils_date
import src.utils.utils_io as utils_io
from src.tasks import timeseriesDB
from src.tasks.database_task import backup_timeseries

_WATTS_SECONDS_TO_KILOWATT_HOURS = 2.778 * math.pow(10, -7)
_TIME_SERIES_FOLDER = "src/time_series"
_HEADER = "created_at,power\n"
_CUTTING_POWER = 10000


def _caching_time_series(device):
    folder_cache = f"src/cache/{device}"
    utils_io.create_folder_if_not_exist(folder_cache)

    path_time_series = f"{_TIME_SERIES_FOLDER}/{device}"
    for doc in utils_io.list_all_files(path_time_series):
        new_path = doc.replace(path_time_series, folder_cache)
        print(f"moving {doc} to {new_path}")
        utils_io.move_file(doc, new_path)


def _put_header(doc):
    _lines = utils_io.read_all_lines(doc)
    utils_io.write_array(doc, [_HEADER, _lines])


def _check_time_series_header(device):
    folder_cache = f"src/cache/{device}"
    for doc in utils_io.list_all_files(folder_cache):
        if _HEADER != utils_io.read_first_line(doc):
            _put_header(doc)
            print(f"put header in {doc}")


def _normalize_data_sets_peaks(device):
    folder_cache = f"src/cache/{device}"
    for doc in utils_io.list_all_files(folder_cache):
        data, peaks = utils_csv.split_data_frame_by_value(doc, 'power', _CUTTING_POWER)
        if len(peaks) > 0:
            max_value = data['power'].max()
            utils_csv.normalize_data_frame_column(doc, 'power', max_value)
            print(doc, f"{len(peaks)} peaks normalized")


def _remove_data_sets_peaks(device):
    folder_cache = f"src/cache/{device}"
    for doc in utils_io.list_all_files(folder_cache):
        data, peaks = utils_csv.split_data_frame_by_value(doc, 'power', _CUTTING_POWER)
        if len(peaks) > 0:
            utils_csv.create_file_csv(doc, data)
            print(doc, f"{len(peaks)} peaks removed")


def _reduce_time_series(device):
    dates = []
    consumptions = []

    folder_cache = f"src/cache/{device}"
    for doc in utils_io.list_all_files(folder_cache):
        data_json = utils_csv.reduce_and_sum(file_csv=doc, column_index='created_at')

        created_at_list = data_json["created_at"]
        consumption_list = data_json["power"]

        for key in created_at_list.keys():
            date = utils_date.timestamp_to_date_string(created_at_list[key])
            dates.append(date)

        for key in consumption_list.keys():
            power = consumption_list[key] * _WATTS_SECONDS_TO_KILOWATT_HOURS
            consumptions.append(power)

        utils_io.delete_file(doc)

    if len(dates) > 0:
        dataframe = utils_csv.create_csv({'date': dates, 'device': device, 'consumption_kwh': consumptions})
        data_json = utils_csv.dataframe_to_json(dataframe)
        timeseriesDB.insert_many(data_json)


def _check_duplicates():
    set_data_consumption = {}
    list_data_consumption = []

    for data_json in timeseriesDB.find_all({}):
        data_json.pop("_id")

        if data_json["date"] in set_data_consumption:
            aux = set_data_consumption[data_json["date"]]
            data_json["consumption_kwh"] += aux["consumption_kwh"]
            set_data_consumption[data_json["date"]] = data_json
        else:
            set_data_consumption[data_json["date"]] = data_json

    for key in set_data_consumption:
        list_data_consumption.append(set_data_consumption[key])

    timeseriesDB.clear()
    timeseriesDB.insert_many(list_data_consumption)


def extract_data():
    print("Step 0: move the time series to cache")
    for device in utils_io.list_sub_folders(_TIME_SERIES_FOLDER):
        print(f"device: {device}")
        _caching_time_series(device)

    print("Step 1: checking if the time series has header")
    for device in utils_io.list_sub_folders(_TIME_SERIES_FOLDER):
        _check_time_series_header(device)

    print("Step 2: normalizing peaks")
    for device in utils_io.list_sub_folders(_TIME_SERIES_FOLDER):
        _normalize_data_sets_peaks(device)

    print("Step 3: reducing if the time series files")
    for device in utils_io.list_sub_folders(_TIME_SERIES_FOLDER):
        _reduce_time_series(device)

    print("Step 4: check duplicates")
    _check_duplicates()

    print("Step 5: backup the time series ")
    backup_timeseries()
