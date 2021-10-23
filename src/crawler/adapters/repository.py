from kingdom_sdk.adapters.repository import BaseRepository
from src.crawler.domain import model


class TracksRepository(BaseRepository):
    _model = model.Track
