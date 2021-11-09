import src.utils.utils_io as utils_io
import src.utils.utils_csv as utils_csv
from src.database import MongoDB

root_folder = "../users/"
base_database = 'smart_energy_'


def _fill_database(database_name, data_directory):
    db = MongoDB(database=database_name, collection="time_series")
    db.clear()

    total_records_size = 0

    for doc in utils_io.list_all_files(data_directory):
        time_series = utils_csv.csv_to_json(doc)

        current_records_size = len(time_series)
        total_records_size += current_records_size

        print("Saving", doc, f"{current_records_size} records")
        db.insert_many(time_series)

    print(f"{database_name} loaded with {total_records_size} records")


for user_name in utils_io.list_sub_folders(root_folder):
    database = base_database + str(user_name).lower()
    directory = f"{root_folder}{user_name}/time_series"
    _fill_database(database, directory)
