import src.utils.utils_io as utils_io
from src.tasks import USERS_FOLDER
from src.tasks.database.task_database_backup import backup_collection
from src.tasks.database.task_database_restore import restore_collection

for user_name in utils_io.list_sub_folders(USERS_FOLDER):
    restore_collection(user_name)

for user_name in utils_io.list_sub_folders(USERS_FOLDER):
    backup_collection(user_name)
