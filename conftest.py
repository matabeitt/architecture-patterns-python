import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from orm import metadata, start_mappers


@pytest.fixture
def local_db():
    engine = create_engine('sqlite:///:memory:')
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session(local_db):
    start_mappers()
    yield sessionmaker(bind=local_db)()
    clear_mappers()
