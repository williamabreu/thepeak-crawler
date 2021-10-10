from abc import ABC, abstractmethod

class AbstractUnitOfWork(ABC):
    def __enter__(self):  # type: ignore
        return self
    def __exit__(self, *args):  # type: ignore
        self.rollback()
    def commit(self) -> None:
        self._commit()
    @abstractmethod
    def _commit(self) -> None:
        raise NotImplementedError
    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError
