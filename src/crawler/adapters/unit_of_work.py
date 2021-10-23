from kingdom_sdk.adapters.unit_of_work import BaseUnitOfWork
from src.crawler.adapters import repository


class CrawlerUnitOfWork(BaseUnitOfWork):
    tracks: repository.TracksRepository
