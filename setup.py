from subprocess import call

import src.domain.utils.utils_io as utils_io


def install_libraries():
    call("pip install " + ' '.join(["--upgrade pip", "setuptools", "wheel"]), shell=True)

    libraries = ["matplotlib", "pandas", "numpy", "pymongo[srv]", "firebase-admin", "pillow", "qrcode", ]
    call("pip install " + ' '.join(libraries), shell=True)
    utils_io.write_array("requirements.txt", [library + "\n" for library in libraries])


if __name__ == '__main__':
    install_libraries()
