from typing import Generator
from sqlalchemy.orm import Session

from chatter.database.base import LocalSession


def get_database() -> Generator[Session, None, None]:
    database = LocalSession()

    try:
        yield database
    finally:
        database.close()
