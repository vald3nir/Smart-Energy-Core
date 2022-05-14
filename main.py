import src.domain.use_cases.database_use_case as database_use_case
import src.domain.use_cases.devices_use_case as devices_use_case
import src.domain.use_cases.time_series_use_case as time_series_use_case


def create_device_code(users_name=None):
    if users_name is None:
        users_name = []
    for user_name in users_name:
        print({"user": user_name, "device code": devices_use_case.create_device_qrcode(user_name)})


def restore_db():
    database_use_case.restore_db()


if __name__ == '__main__':
    # restore_db()
    time_series_use_case.extract_data()
    database_use_case.backup_db()
    database_use_case.export_time_series_to_firebase()
    print("Finish!")
