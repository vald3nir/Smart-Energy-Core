import src.utils.utils_csv as utils_csv
import src.utils.utils_date as utils_date
import src.utils.utils_io as utils_io
from src.database import MongoDB
from src.tasks.constants import *


def reduce_time_series(_user_name):
    db = MongoDB(collection=f"{_user_name}_TimeSeries")
    # db.clear()

    # timeline_directory_base = f"{USERS_FOLDER}{_user_name}/timeline/"
    # utils_io.create_folder_if_not_exist(timeline_directory_base)

    time_series_directory = get_path_time_series(_user_name)

    for doc in utils_io.list_all_files(time_series_directory):
        data_json = utils_csv.reduce_and_sum(file_csv=doc, column_index='created_at')

        dates = []
        consumptions = []

        created_at_list = data_json["created_at"]
        consumption_list = data_json["power"]

        for key in created_at_list.keys():
            date = utils_date.timestamp_to_date(created_at_list[key])
            dates.append(date)

        for key in consumption_list.keys():
            power = consumption_list[key] * WATTS_SECONDS_TO_KILOWATT_HOURS
            consumptions.append(power)

        _, file = utils_io.split_path_file(doc)

        time_series_summary_file = utils_io.join_path_file(time_series_directory, file)
        fields = {'date': dates, 'consumption_kwh': consumptions}

        utils_csv.create_file_csv(file_path=time_series_summary_file, fields=fields)
