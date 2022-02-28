import src.utils.utils_csv as utils_csv
import src.utils.utils_io as utils_io
from src.database.Firebase import FirebaseDB
from src.database.MongoDB import MongoDB

# -------------------------------------------------------------------
# USERS
# -------------------------------------------------------------------

USERS_CSV = "src/database/backup/users.csv"


def _backup_users():
    db = MongoDB("users")
    data_list_json = []

    for data_json in db.find_all({}):
        data_json.pop("_id")
        data_list_json.append(data_json)

    utils_csv.json_to_file_csv(USERS_CSV, data_list_json)


def _restore_users():
    db = MongoDB(collection="users")
    db.clear()
    db.insert_many(utils_csv.file_csv_to_json(USERS_CSV))


# -------------------------------------------------------------------
# CONSUMPTION
# -------------------------------------------------------------------

def _backup_consumption():
    db = MongoDB("consumption")

    for device in db.distinct("device"):
        consumption = []

        for data_json in db.find_all({"device": device}):
            data_json.pop("_id")
            consumption.append(data_json)

        file_csv = f"src/database/backup/{device}.csv"
        utils_csv.json_to_file_csv(file_csv, consumption)


def _restore_consumption():
    db = MongoDB(collection="consumption")
    db.clear()
    for file_csv in utils_io.list_all_files("src/database/backup/"):
        if file_csv != USERS_CSV:
            data_json = utils_csv.file_csv_to_json(file_csv)
            db.insert_many(data_json)


# -------------------------------------------------------------------
# ALL
# -------------------------------------------------------------------

def export_data_to_firebase():
    db = FirebaseDB()
    db.clear()
    for file_csv in utils_io.list_all_files("src/database/backup/"):
        if file_csv != USERS_CSV:
            data_json = utils_csv.file_csv_to_json(file_csv)
            db.insert(header="consumption", collection=data_json[0]["device"], data=data_json)


def backup_collections():
    _backup_users()
    _backup_consumption()


def restore_collections():
    _restore_users()
    _restore_consumption()
