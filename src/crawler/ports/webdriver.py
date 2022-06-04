from abc import ABC, abstractmethod
from typing import List

from src.crawler.domain.models import Track


class Webdriver(ABC):
    @abstractmethod
    def run(self) -> List[Track]:
        raise NotImplementedError
