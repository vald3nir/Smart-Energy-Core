from src.utils.setup_utils import load_libraries

if __name__ == '__main__':
    load_libraries(libraries=[
        "setuptools", "wheel",
        "matplotlib", "pandas", "numpy",
        "pymongo[srv]"
    ])
