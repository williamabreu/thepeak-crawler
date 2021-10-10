from abc import ABC, abstractmethod

class AbstractUnitOfWork(ABC):
    def __init__(self):  # type: ignore
        self.errors = []
    def __enter__(self):  # type: ignore
        return self
    def __exit__(self, *args):  # type: ignore
        self.rollback()
    def commit(self) -> None:
        """Every time a commit is made, we try to commit current database
        transaction"""
        self._commit()
    @abstractmethod
    def _commit(self) -> None:
        raise NotImplementedError
    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError
