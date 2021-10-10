import os
from importlib.machinery import SourceFileLoader

from sqlalchemy import MetaData

from src import get_src_dir
from src.core.utils import find_files


def start_mappers(metadata: MetaData) -> MetaData:
    src_dir = get_src_dir()

    orm_files = find_files(
        file_name="orm.py",
        base_dir=src_dir,
        excluded_dirs=[os.path.join(src_dir, "core")],
    )

    for path in orm_files:
        module = SourceFileLoader("start_mappers", path).load_module()
        module.start_mappers(metadata)  # type: ignore

    return metadata
