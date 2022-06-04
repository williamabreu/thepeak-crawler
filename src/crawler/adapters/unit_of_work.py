from kingdom_sdk.adapters.unit_of_work import SQLAlchemyUnitOfWork

from src.crawler.adapters import repository


class CrawlerUnitOfWork(SQLAlchemyUnitOfWork):
    tracks: repository.TracksRepository
