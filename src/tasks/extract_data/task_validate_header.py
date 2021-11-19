import src.utils.utils_io as utils_io
from src.tasks import get_path_time_series

_header = "created_at,power\n"


def _put_header(doc):
    _lines = utils_io.read_all_lines(doc)
    utils_io.write_array(doc, [_header, _lines])


def check_time_series_header(_user_name):
    for doc in utils_io.list_all_files(get_path_time_series(_user_name)):
        if _header != utils_io.read_first_line(doc):
            _put_header(doc)
            print(f"put header in {doc}")
