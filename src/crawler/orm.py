from kingdom_sdk.database.factories import aggregate_table_factory
from kingdom_sdk.database.mappers import aggregate_mapper
from sqlalchemy import Column, DateTime, MetaData, String

from src.crawler.domain import model

tracks = aggregate_table_factory(
    "tracks",
    Column("timestamp", DateTime(), nullable=False),
    Column("artist", String(255), nullable=False),
    Column("title", String(255), nullable=False),
)


def start_mappers(metadata: MetaData) -> None:
    tracks_t = tracks(metadata)
    aggregate_mapper(model.Track, tracks_t)
