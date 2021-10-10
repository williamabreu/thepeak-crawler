from datetime import datetime

from src.core.domain.models import Aggregate


class Track(Aggregate):
    id: int
    song_time: datetime
    song_artist: str
    song_title: str

    def __init__(self, song_time: datetime, song_artist: str, song_title: str):
        super().__init__()  # type: ignore
        self.song_time = song_time
        self.song_artist = song_artist
        self.song_title = song_title
