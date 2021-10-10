from typing import Any, Dict, Tuple

from dotenv import load_dotenv
from sqlalchemy import MetaData

from src.core.orm import start_mappers

load_dotenv()

AnyDict = Dict[Any, Any]


def federation(**dependencies: AnyDict) -> Tuple[MetaData, AnyDict, AnyDict]:
    metadata = MetaData()
    start_mappers(metadata)
    return metadata, {}, {}
