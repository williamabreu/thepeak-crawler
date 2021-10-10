from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker

from src.config import get_postgres_uri
from src.core.ports.unit_of_work import AbstractUnitOfWork

DEFAULT_SESSION_FACTORY = orm.sessionmaker(
    bind=create_engine(
        # ISOLATION LEVEL ENSURES aggregate's version IS RESPECTED
        # That is, if version differs it will raise an exception
        get_postgres_uri(),
        isolation_level="REPEATABLE_READ",
    ),
    autoflush=False,
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    session: orm.Session

    def __init__(
        self, session_factory: sessionmaker = DEFAULT_SESSION_FACTORY
    ):
        super().__init__()  # type: ignore
        self.session_factory: sessionmaker = session_factory

    def __exit__(self, *args):  # type: ignore
        super().__exit__(*args)  # type: ignore
        self.session.close()

    def _commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
