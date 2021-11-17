import src.utils.utils_io as utils_io
from src.tasks.constants import get_path_time_series

header = "created_at,device_id,power\n"


def _put_header(doc):
    _lines = utils_io.read_all_lines(doc)
    utils_io.write_array(doc, [header, _lines])


def check_time_series_header(_user_name):
    for doc in utils_io.list_all_files(get_path_time_series(_user_name)):
        if header != utils_io.read_first_line(doc):
            _put_header(doc)
            print(f"put header in {doc}")
