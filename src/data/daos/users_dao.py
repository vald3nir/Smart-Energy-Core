from src.constants import USERS_CSV
from src.data.database.MongoDB import MongoDB
from src.domain.utils import utils_csv


class UsersDAO(MongoDB):

    def __init__(self) -> None:
        super().__init__("users")

    def backup(self):
        data_list_json = []

        for data_json in self.find_all({}):
            data_json.pop("_id")
            data_list_json.append(data_json)

        utils_csv.json_to_file_csv(USERS_CSV, data_list_json)

    def restore(self):
        self.clear()
        self.insert_many(utils_csv.file_csv_to_json(USERS_CSV))
