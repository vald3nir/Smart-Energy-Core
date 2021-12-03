from src.database import MongoDB
from src.tasks import get_time_series_collection_name


def check_duplicates(_user_name):
    db = MongoDB(collection=get_time_series_collection_name(_user_name))

    set_data_consumption = {}
    list_data_consumption = []

    for data_json in db.find_all({}):
        data_json.pop("_id")

        if data_json["date"] in set_data_consumption:
            aux = set_data_consumption[data_json["date"]]
            data_json["consumption_kwh"] += aux["consumption_kwh"]
            set_data_consumption[data_json["date"]] = data_json
        else:
            set_data_consumption[data_json["date"]] = data_json

    for key in set_data_consumption:
        list_data_consumption.append(set_data_consumption[key])

    db.clear()
    db.insert_many(list_data_consumption)
