from importlib.machinery import SourceFileLoader

from sqlalchemy import MetaData

from src import get_src_dir
from src.core.utils import find_files


def start_mappers(metadata: MetaData) -> MetaData:
    orm_files = find_files("orm.py", get_src_dir())

    for path in orm_files:
        module = SourceFileLoader("start_mappers", path).load_module()
        module.start_mappers(metadata)  # type: ignore

    return metadata
