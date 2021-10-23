from typing import Any, Dict, Tuple

from dotenv import load_dotenv
from sqlalchemy import MetaData
from kingdom_sdk.database import orm

load_dotenv()


def federation(**dependencies: Any) -> Tuple[MetaData, Dict, Dict]:
    metadata = orm.start_mappers('src.crawler.orm')
    return metadata, {}, {}
