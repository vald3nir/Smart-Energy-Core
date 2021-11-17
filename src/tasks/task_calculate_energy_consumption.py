import src.utils.utils_csv as utils_csv
import src.utils.utils_io as utils_io
from src.database import MongoDB
from src.tasks import *


def _fill_energy_consumption(_user_name):
    time_series_directory = f"{USERS_FOLDER}{_user_name}/time_series"
    consumption_directory = f"{USERS_FOLDER}{_user_name}/consumption_summary"

    consumption_summary = {}
    consumption_array = []

    for doc in utils_io.list_all_files(time_series_directory):
        date = doc.replace(time_series_directory, "")[9:-4]
        file_name = f"{date[:4]}-{date[5:7]}"

        consumption = {
            "date": date,
            "consumption": WATTS_SECONDS_TO_KILOWATT_HOURS * utils_csv.sum_columns(doc, "power")
        }

        consumption_array.append(consumption)

        if file_name not in consumption_summary:
            consumption_summary[file_name] = []
        consumption_summary[file_name].append(consumption)

    for key in consumption_summary:
        folder = f"{consumption_directory}/{key[:4]}"
        utils_io.create_folder_if_not_exist(folder)
        # to-do: verificar se já exite o arquivo, caso sim, adicionar ao final do array
        utils_io.write_json(f"{folder}/{key[5:]}.json", consumption_summary[key])

    if len(consumption_array) > 0:
        db = MongoDB(collection=f"{_user_name}_Consumption")
        # db.clear()
        db.insert_many(consumption_array)


if __name__ == '__main__':
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        _fill_energy_consumption(user_name)
