from typing import List, Optional, Union

from src.core.adapters.repository import BaseRepository
from src.core.domain.models import Aggregate
from src.crawler.domain import models


class TracksRepository(BaseRepository):
    def _list(self) -> List[Aggregate]:
        return self.session.query(models.Track).all()  # type: ignore

    def _get(self, id: Union[int, str]) -> Optional[Aggregate]:
        return (  # type: ignore
            self.session.query(models.Track)
            .filter(models.Track.id == id)
            .first()
        )
