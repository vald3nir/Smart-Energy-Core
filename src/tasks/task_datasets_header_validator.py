import src.utils.utils_io as utils_io

root_folder = "../users/"
header = "created_at,device_id,power\n"


def _check_file_has_header(doc):
    f = open(doc, "r")
    _header = f.readline()
    f.close()
    return header == _header


def _put_header(doc):
    f = open(doc, "r")
    _lines = f.read()
    f.close()

    f = open(doc, "w")
    f.write(header)
    f.write(_lines)
    f.close()


def _fill_headers(_user_name):
    data_directory = f"{root_folder}{_user_name}/time_series"
    for doc in utils_io.list_all_files(data_directory):
        if not _check_file_has_header(doc):
            _put_header(doc)
            print(f"put header in {doc}")


if __name__ == '__main__':
    for user_name in utils_io.list_sub_folders(root_folder):
        _fill_headers(user_name)
