from src.core.adapters.unit_of_work import BaseUnitOfWork
from src.crawler.adapters import repository


class CrawlerUnitOfWork(BaseUnitOfWork):
    tracks: repository.TracksRepository

    def __enter__(self):  # type: ignore
        super().__enter__()  # type: ignore
        self.tracks = repository.TracksRepository(self.session)
        return self
