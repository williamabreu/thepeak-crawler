from kingdom_sdk.database.factories import aggregate_table_factory
from kingdom_sdk.database.mappers import aggregate_mapper
from sqlalchemy import Column, DateTime, MetaData, String

from src.crawler.domain import models

tracks = aggregate_table_factory(
    "tracks",
    Column("timestamp", DateTime(), nullable=False),
    Column("artist", String(255), nullable=False),
    Column("title", String(255), nullable=False),
    schema="crawler",
)


def start_mappers(metadata: MetaData) -> None:
    tracks_t = tracks(metadata)
    aggregate_mapper(models.Track, tracks_t)
