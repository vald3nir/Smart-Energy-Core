import os


# def list_all_files(directory):
#     _files = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             _files.append(os.path.join(root, file))
#             # _files.append(file)
#     return _files

def list_sub_folders(directory):
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]


def list_all_files(directory):
    list_files = os.listdir(directory)
    all_files = list()

    for entry in list_files:
        full_path = os.path.join(directory, entry)

        if os.path.isdir(full_path):
            all_files = all_files + list_all_files(full_path)

        else:
            all_files.append(full_path)

    return all_files


def check_if_file_exist(file):
    return os.path.isfile(file)


def create_folder_if_not_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def list_files_with_prefix(folder, prefix):
    files = [f for f in os.listdir(folder) if
             str(f).__contains__(prefix) and check_if_file_exist(os.path.join(folder, f))
             ]
    return files
