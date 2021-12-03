import src.utils.utils_csv as utils_csv
from src.database import MongoDB
from src.tasks import get_path_consumption_summary, get_time_series_collection_name


def check_duplicates(_user_name):
    db = MongoDB(collection=get_time_series_collection_name(_user_name))

