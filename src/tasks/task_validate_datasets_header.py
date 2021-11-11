import src.utils.utils_io as utils_io
from src.tasks import USERS_FOLDER

header = "created_at,device_id,power\n"


def _put_header(doc):
    _lines = utils_io.read_all_lines(doc)
    utils_io.write_array(doc, [header, _lines])


def _fill_headers(_user_name):
    data_directory = f"{USERS_FOLDER}{_user_name}/time_series"
    for doc in utils_io.list_all_files(data_directory):
        if header != utils_io.read_first_line(doc):
            _put_header(doc)
            print(f"put header in {doc}")


if __name__ == '__main__':
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        _fill_headers(user_name)
