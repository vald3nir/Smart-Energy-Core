from src.tasks.device_task import create_new_user_with_device
from src.tasks.export_firebase_task import export_data_to_firebase
from src.tasks.extract_data_task import extract_data

if __name__ == '__main__':
    # create_new_user_with_device(["new_user"])
    extract_data()
    # export_data_to_firebase()
    print("Finish!")
