from datetime import datetime


class Track:
    id: int
    song_time: datetime
    song_artist: str
    song_title: str

    def __init__(self, song_time: datetime, song_artist: str, song_title: str):
        self.song_time = song_time
        self.song_artist = song_artist
        self.song_title = song_title
