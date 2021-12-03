import src.utils.utils_csv as utils_csv
from src.database import MongoDB
from src.tasks import get_path_consumption_summary, get_time_series_collection_name


def restore_collection(_user_name):
    db = MongoDB(collection=get_time_series_collection_name(_user_name))
    db.clear()

    file_csv = get_path_consumption_summary(_user_name)
    data_json = utils_csv.file_csv_to_json(file_csv)

    db.insert_many(data_json)
