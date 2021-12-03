import src.utils.utils_csv as utils_csv
from src.database import MongoDB
from src.tasks import get_path_consumption_summary, get_time_series_collection_name


def backup_collection(_user_name):
    db = MongoDB(collection=get_time_series_collection_name(_user_name))

    data_list_json = []

    for data_json in db.find_all({}):
        data_json.pop("_id")
        data_list_json.append(data_json)

    file_csv = get_path_consumption_summary(_user_name)
    utils_csv.json_to_file_csv(file_csv, data_list_json)
