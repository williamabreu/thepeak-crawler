from typing import Callable

from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table
from sqlalchemy.orm import mapper

from src.crawler.domain import models

tracks: Callable[[MetaData], Table] = lambda metadata: Table(
    "tracks",
    metadata,
    Column(
        "id", Integer(), primary_key=True, autoincrement=True, nullable=False
    ),
    Column("song_time", DateTime(), nullable=False),
    Column("song_artist", String(128), nullable=False),
    Column("song_title", String(128), nullable=False),
)


def start_mappers(metadata: MetaData) -> MetaData:
    tracks_t = tracks(metadata)
    mapper(models.Track, tracks_t)
    return metadata
