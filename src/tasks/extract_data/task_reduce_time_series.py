import math

import src.utils.utils_csv as utils_csv
import src.utils.utils_date as utils_date
import src.utils.utils_io as utils_io
from src.database import MongoDB
from src.tasks import *

WATTS_SECONDS_TO_KILOWATT_HOURS = 2.778 * math.pow(10, -7)


def reduce_time_series(_user_name):
    dates = []
    consumptions = []

    for doc in utils_io.list_all_files(get_path_time_series(_user_name)):
        data_json = utils_csv.reduce_and_sum(file_csv=doc, column_index='created_at')

        created_at_list = data_json["created_at"]
        consumption_list = data_json["power"]

        for key in created_at_list.keys():
            date = utils_date.timestamp_to_date_string(created_at_list[key])
            dates.append(date)

        for key in consumption_list.keys():
            power = consumption_list[key] * WATTS_SECONDS_TO_KILOWATT_HOURS
            consumptions.append(power)

        utils_io.delete_file(doc)

    if len(dates) > 0:
        dataframe = utils_csv.create_csv({'date': dates, 'consumption_kwh': consumptions})
        data_json = utils_csv.dataframe_to_json(dataframe)

        db = MongoDB(collection=get_time_series_collection_name(_user_name))
        db.insert_many(data_json)
