from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session as Session

from chatter.config import Config

engine = create_engine(Config.DATABASE_URL, connect_args={
    "check_same_thread": False})

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseEntity = declarative_base()


def create_database() -> None:
    BaseEntity.metadata.create_all(bind=engine)
