import math

import src.domain.utils.utils_csv as utils_csv
import src.domain.utils.utils_date as utils_date
import src.domain.utils.utils_io as utils_io
from src.data.daos.time_series_dao import TimeSeriesDAO


# ======================================================================================================================

def _caching_time_series():
    origin_folder = "P://Documents//time_series"
    for device_name in utils_io.list_sub_folders(origin_folder):
        print(f"device: {device_name}")

        folder_time_series = f"{origin_folder}/{device_name}"
        folder_cache = f"cache/{device_name}"
        utils_io.move_file(folder_time_series, folder_cache)


# ======================================================================================================================

def _delete_files_cached():
    for item in utils_io.list_all_files("cache"):
        utils_io.delete_file(item)


def _list_all_times_series():
    return utils_io.list_all_files("cache")


# ======================================================================================================================


def _check_time_series_header():
    _HEADER = "created_at,power\n"
    for doc in _list_all_times_series():
        if _HEADER != utils_io.read_first_line(doc):
            _lines = utils_io.read_all_lines(doc)
            utils_io.write_array(doc, [_HEADER, _lines])
            print(f"put header in {doc}")


# ======================================================================================================================

def _normalize_data_sets_peaks():
    _CUTTING_POWER = 10000
    for doc in _list_all_times_series():
        data, peaks = utils_csv.split_data_frame_by_value(doc, 'power', _CUTTING_POWER)
        if len(peaks) > 0:
            max_value = data['power'].max()
            utils_csv.normalize_data_frame_column(doc, 'power', max_value)
            print(doc, f"{len(peaks)} peaks normalized")


# ======================================================================================================================

def _reduce_time_series():
    _WATTS_SECONDS_TO_KILOWATT_HOURS = 2.778 * math.pow(10, -7)

    _dates = []
    _consumptions = []

    _timeseriesDB = TimeSeriesDAO()

    for doc in _list_all_times_series():
        device = doc.split("\\")[1]
        data_json = utils_csv.reduce_and_sum(file_csv=doc, column_index='created_at')

        created_at_list = data_json["created_at"]
        consumption_list = data_json["power"]

        for key in created_at_list.keys():
            date = utils_date.timestamp_to_date_string(created_at_list[key])
            _dates.append(date)

        for key in consumption_list.keys():
            power = consumption_list[key] * _WATTS_SECONDS_TO_KILOWATT_HOURS
            _consumptions.append(power)

        if len(_dates) > 0:
            dataframe = utils_csv.create_csv({'date': _dates, 'device': device, 'consumption_kwh': _consumptions})
            data_json = utils_csv.dataframe_to_json(dataframe)
            print(data_json)

            _timeseriesDB.insert_many(data_json)

        _dates = []
        _consumptions = []


# ======================================================================================================================

def _check_duplicates():
    set_data_consumption = {}
    list_data_consumption = []

    _timeseriesDB = TimeSeriesDAO()

    for data_json in _timeseriesDB.find_all({}):
        data_json.pop("_id")

        if data_json["date"] in set_data_consumption:
            aux = set_data_consumption[data_json["date"]]
            data_json["consumption_kwh"] += aux["consumption_kwh"]
            set_data_consumption[data_json["date"]] = data_json
        else:
            set_data_consumption[data_json["date"]] = data_json

    for key in set_data_consumption:
        list_data_consumption.append(set_data_consumption[key])

    _timeseriesDB.clear()
    _timeseriesDB.insert_many(list_data_consumption)


# ======================================================================================================================

def extract_data():
    print("Step 0: move the time series to cache")
    _caching_time_series()
    print("Step 1: checking if the time series has header")
    _check_time_series_header()
    print("Step 2: normalizing peaks")
    _normalize_data_sets_peaks()
    print("Step 3: reducing if the time series files")
    _reduce_time_series()
    print("Step 4: check duplicates")
    _check_duplicates()
    # print("Step 5: delete cache")
    # _delete_files_cached()
