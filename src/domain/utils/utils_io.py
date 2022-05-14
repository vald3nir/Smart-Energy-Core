import json
import os
import shutil


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


def split_path_file(doc):
    return os.path.split(doc)


def join_path_file(folder, doc):
    return os.path.join(folder, doc)


def create_folder_if_not_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def read_first_line(file):
    f = open(file, "r")
    line = f.readline()
    f.close()
    return line


def read_all_lines(file):
    f = open(file, "r")
    lines = f.read()
    f.close()
    return lines


def write_json(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write_array(file, lines):
    f = open(file, "w")
    for line in lines:
        f.write(line)
    f.close()


def delete_file(file_path):
    os.remove(file_path)


def move_folder(folder_path, new_path):
    move_file(folder_path, new_path)


def move_file(file_path, new_path):
    shutil.move(file_path, new_path)
