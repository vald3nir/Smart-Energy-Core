from src.tasks.export_firebase_task import export_data_to_firebase
from src.tasks.extract_data_task import extract_data

if __name__ == '__main__':
    extract_data()
    export_data_to_firebase()
    print("Finish!")
