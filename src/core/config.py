import os
from typing import Optional


def get_postgres_uri() -> Optional[str]:
    return os.environ.get("DATABASE_URL")
