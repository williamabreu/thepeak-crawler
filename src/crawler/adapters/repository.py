from kingdom_sdk.adapters.repository import SQLAlchemyRepository

from src.crawler.domain import models


class TracksRepository(SQLAlchemyRepository):
    _model = models.Track
