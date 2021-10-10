from abc import ABC, abstractmethod
from typing import List, Optional, Union

from src.core.domain.models import Aggregate


class AbstractRepository(ABC):
    def add(self, aggregate: Aggregate) -> None:
        return self._add(aggregate)

    def list(self) -> List[Aggregate]:
        return self._list()

    def get(self, id: Union[int, str]) -> Optional[Aggregate]:
        return self._get(id)

    @abstractmethod
    def _add(self, aggregate: Aggregate) -> None:
        raise NotImplementedError

    @abstractmethod
    def _list(self) -> List[Aggregate]:
        raise NotImplementedError

    @abstractmethod
    def _get(self, id: Union[int, str]) -> Optional[Aggregate]:
        raise NotImplementedError
