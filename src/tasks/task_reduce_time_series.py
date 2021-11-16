import src.utils.utils_csv as utils_csv
import src.utils.utils_date as utils_date
import src.utils.utils_io as utils_io
from src.database import MongoDB
from src.tasks.constants import *


def reduce_time_series(_user_name):
    dates = []
    consumptions = []

    for doc in utils_io.list_all_files(get_path_time_series(_user_name)):
        data_json = utils_csv.reduce_and_sum(file_csv=doc, column_index='created_at')

        created_at_list = data_json["created_at"]
        consumption_list = data_json["power"]

        for key in created_at_list.keys():
            date = utils_date.timestamp_to_date(created_at_list[key])
            dates.append(date)

        for key in consumption_list.keys():
            power = consumption_list[key] * WATTS_SECONDS_TO_KILOWATT_HOURS
            consumptions.append(power)

    if len(dates) > 0:
        time_series_summary_file = utils_io.join_path_file(get_path_consumption_summary(_user_name), "time_series.csv")
        fields = {'date': dates, 'consumption_kwh': consumptions}

        utils_csv.create_file_csv(file_path=time_series_summary_file, fields=fields)

        time_series_json = utils_csv.csv_to_json(time_series_summary_file)

        db = MongoDB(collection=f"{_user_name}_TimeSeries")
        db.insert_many(time_series_json)
