import src.utils.utils_csv as utils_csv
from src.tasks import *


# -------------------------------------------------------------------
# USERS
# -------------------------------------------------------------------

def backup_users():
    data_list_json = []

    for data_json in userDB.find_all({}):
        data_json.pop("_id")
        data_list_json.append(data_json)

    utils_csv.json_to_file_csv(USERS_CSV, data_list_json)


def _restore_users():
    userDB.clear()
    userDB.insert_many(utils_csv.file_csv_to_json(USERS_CSV))


# -------------------------------------------------------------------
# Timeseries
# -------------------------------------------------------------------

def backup_timeseries():
    consumption = []

    for data_json in timeseriesDB.find_all(query={}, sort_field="date"):
        data_json.pop("_id")
        consumption.append(data_json)

    utils_csv.json_to_file_csv(TIME_SERIES_CSV, consumption)


def _restore_timeseries():
    timeseriesDB.clear()
    timeseriesDB.insert_many(utils_csv.file_csv_to_json(TIME_SERIES_CSV))


# -------------------------------------------------------------------
# Restore all collections
# -------------------------------------------------------------------


def restore_collections():
    _restore_users()
    _restore_timeseries()


# if __name__ == '__main__':
#     restore_collections()
