import math

import src.utils.utils_csv as utils_csv
import src.utils.utils_io as utils_io
from src.database import MongoDBLocal, MongoDBRemote
from src.tasks import USERS_FOLDER

DATABASE_NAME = 'smart_energy'
WATTS_SECONDS_TO_KILOWATT_HOURS = 2.778 * math.pow(10, -7)


def _fill_energy_consumption(_user_name):
    time_series_directory = f"{USERS_FOLDER}{_user_name}/time_series"
    consumption_json_file = f"{USERS_FOLDER}{_user_name}/consumption.json"

    consumption_array = []
    for doc in utils_io.list_all_files(time_series_directory):
        consumption = {
            "date": doc.replace(time_series_directory, "")[9:-4],
            "consumption": WATTS_SECONDS_TO_KILOWATT_HOURS * utils_csv.sum_columns(doc, "power")
        }
        print(consumption)
        consumption_array.append(consumption)

    if len(consumption_array) > 0:
        utils_io.write_json(consumption_json_file, consumption_array)

        db = MongoDBRemote(database=DATABASE_NAME, collection=f"{_user_name}_consumption")
        db.clear()
        db.insert_many(consumption_array)


def _fill_time_series(_user_name):
    db = MongoDBLocal(database=DATABASE_NAME, collection=f"{_user_name}_time_series")
    db.clear()

    total_records_size = 0

    data_directory = f"{USERS_FOLDER}{_user_name}/time_series"
    for doc in utils_io.list_all_files(data_directory):
        time_series = utils_csv.csv_to_json(doc)

        current_records_size = len(time_series)
        total_records_size += current_records_size

        print("Saving", doc, f"{current_records_size} records")
        db.insert_many(time_series)

    print(f"{DATABASE_NAME} loaded with {total_records_size} time series")


def _fill_database(_user_name):
    # _fill_time_series(_user_name)
    _fill_energy_consumption(_user_name)


if __name__ == '__main__':
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        _fill_database(user_name)
