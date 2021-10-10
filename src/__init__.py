import os

__name__ = "src"
__version__ = "1.0dev1"


def get_base_dir() -> str:
    path, _ = os.path.split(os.path.dirname(__file__))
    return path


def get_src_dir() -> str:
    return os.path.dirname(__file__)
