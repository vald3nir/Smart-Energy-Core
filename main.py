from subprocess import call

import src.utils.utils_io as utils_io
from src.tasks.database_task import restore_collections
from src.tasks.device_task import create_new_user_with_device
from src.tasks.export_firebase_task import export_data_to_firebase
from src.tasks.extract_data_task import extract_data


def install_libraries():
    call("pip install " + ' '.join(["--upgrade pip", "setuptools", "wheel"]), shell=True)

    libraries = ["matplotlib", "pandas", "numpy", "pymongo[srv]", "firebase-admin", "pillow", "qrcode", ]
    call("pip install " + ' '.join(libraries), shell=True)
    utils_io.write_array("requirements.txt", [library + "\n" for library in libraries])


if __name__ == '__main__':
    # install_libraries()
    # restore_collections()
    # create_new_user_with_device(["new_user"])
    extract_data()
    # export_data_to_firebase()
    print("Finish!")
