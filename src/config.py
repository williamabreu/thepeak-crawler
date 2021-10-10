import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


def get_postgres_uri() -> Optional[str]:
    return os.environ.get("DATABASE_URL")
