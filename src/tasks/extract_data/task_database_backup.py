import src.utils.utils_csv as utils_csv
from src.database import MongoDB
from src.tasks import get_path_consumption_summary


def backup_collection(_user_name):
    db = MongoDB(collection=f"{_user_name}_TimeSeries")

    data_list_json = []

    for data_json in db.find_all({}):
        data_json.pop("_id")
        data_list_json.append(data_json)

    file_csv = get_path_consumption_summary(_user_name)
    utils_csv.json_to_file_csv(file_csv, data_list_json)
