from __future__ import annotations
from datetime import datetime
from typing import Any
from uuid import uuid4

from kingdom_sdk.domain.aggregate import Aggregate
from kingdom_sdk.utils import time


class Track(Aggregate):
    _timestamp: datetime
    _artist: str
    _title: str

    __slots__ = ('_timestamp', '_artist', '_title')

    def __init__(
        self,
        id: UUID,  # noqa
        version: int,
        is_discarded: bool,
        registered_at: datetime,
        updated_at: datetime,
        timestamp: datetime,
        artist: str,
        title: str
    ) -> None:
        super().__init__(id, version, is_discarded, registered_at, updated_at)
        self._timestamp = timestamp
        self._artist = artist
        self._title = title

    @classmethod
    def create(cls, song_time: datetime, song_artist: str, song_title: str) -> Track:
        now = time.generate_now()
        return cls(
            id=uuid4(),
            version=0,
            is_discarded=False,
            registered_at=now,
            updated_at=now,
            timestamp=song_time,
            artist=song_artist,
            title=song_title,
        )

    def __repr__(self) -> str:
        return self._base_repr(self.id.hex)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Track):
            return self.id == other.id
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.id)

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def artist(self) -> str:
        return self._artist

    @property
    def title(self) -> str:
        return self._title
