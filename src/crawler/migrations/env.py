# type: ignore

import os
import sys
from logging.config import fileConfig

from alembic import context
from kingdom_sdk.database.migrations import (
    run_migrations_offline,
    run_migrations_online,
)
from kingdom_sdk.database.orm import start_mappers
from sqlalchemy import orm

# This is the Alembic Config object,
# which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Add your model's MetaData object here.
# For 'autogenerate' support:
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
orm.clear_mappers()
sys.path.insert(0, os.getcwd())
target_metadata = start_mappers("src.crawler.orm")

# Postgres schema name, where the "alembic_version" table will be stored.
SCHEMA_NAME = "crawler"

# Other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


if context.is_offline_mode():
    run_migrations_offline(target_metadata, SCHEMA_NAME)
else:
    run_migrations_online(target_metadata, SCHEMA_NAME)
