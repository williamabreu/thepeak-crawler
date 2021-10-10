from typing import Any, List


class ValueObject:
    pass


class Entity:
    pass


class Aggregate:
    _events: List[Any]
    _version: int

    def __init__(self):  # type: ignore
        self._events = []
        self._version = 0
