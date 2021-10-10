from typing import Any, Dict, Tuple

from sqlalchemy import MetaData

from src.orm import start_mappers

AnyDict = Dict[Any, Any]


def federation(**dependencies: AnyDict) -> Tuple[MetaData, AnyDict, AnyDict]:
    metadata = MetaData()
    start_mappers(metadata)
    return metadata, {}, {}
