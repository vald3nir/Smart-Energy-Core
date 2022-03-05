from subprocess import call

import src.utils.utils_io as utils_io

if __name__ == '__main__':
    call("pip install " + ' '.join(["--upgrade pip", "setuptools", "wheel"]), shell=True)

    libraries = ["matplotlib", "pandas", "numpy", "pymongo[srv]", "firebase-admin", "pillow", "qrcode", ]
    call("pip install " + ' '.join(libraries), shell=True)
    utils_io.write_array("requirements.txt", [library + "\n" for library in libraries])
