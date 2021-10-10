from abc import ABC
from typing import Optional, Set, Union

from sqlalchemy.orm import Session

from src.core.domain.models import Aggregate
from src.core.ports.repository import AbstractRepository


class BaseRepository(AbstractRepository, ABC):
    session: Session
    seen: Set[Aggregate]

    def __init__(self, session: Session):
        self.seen: Set[Aggregate] = set()
        self.session = session

    def add(self, aggregate: Aggregate) -> None:
        self.seen.add(aggregate)
        self._add(aggregate)

    def get(self, id: Union[int, str]) -> Optional[Aggregate]:
        aggregate = self._get(id)
        if aggregate:
            self.seen.add(aggregate)
        return aggregate

    def _add(self, aggregate: Aggregate) -> None:
        self.session.add(aggregate)
