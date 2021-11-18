import src.utils.utils_io as utils_io
from src.tasks import USERS_FOLDER
from src.tasks.database.task_database_backup import backup_collection
from src.tasks.database.task_database_restore import restore_collection


def run_restore_database():
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        restore_collection(user_name)
    print("Database restored")


def run_backup_collection():
    for user_name in utils_io.list_sub_folders(USERS_FOLDER):
        backup_collection(user_name)
    print("Backup finished")


if __name__ == '__main__':
    # run_restore_database()
    run_backup_collection()
