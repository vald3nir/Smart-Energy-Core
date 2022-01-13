from subprocess import call

import src.utils.utils_io as utils_io


def load_libraries(libraries):
    call("pip install " + ' '.join(libraries), shell=True)
    # call("pip freeze > requirements.txt", shell=True)
    utils_io.write_array("requirements.txt", [l + "\n" for l in libraries])
