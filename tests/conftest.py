import psycopg2
import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from data.db.settings import db_settings
from data.uow.sql_orm_uow import SQLORMUnitOfWork
from data.db.models.author import Author  # noqa
from data.db.models.base import Base

# Clone the database settings and set up the test database
test_db_settings = db_settings.model_copy()
test_db_settings.DB_NAME = "test_db"


class FakeUnitOfWork(SQLORMUnitOfWork):
    def __init__(self, session_factory):
        self._session_factory = session_factory


def create_test_db():
    conn = psycopg2.connect(
        dbname=db_settings.DB_NAME,
        user=db_settings.DB_USER,
        password=db_settings.DB_PASS,
        host=db_settings.DB_HOST,
    )
    conn.autocommit = True
    cur = conn.cursor()

    try:
        cur.execute(f"CREATE DATABASE {test_db_settings.DB_NAME}")
    except psycopg2.errors.DuplicateDatabase:
        pass
    finally:
        cur.close()
        conn.close()


def drop_test_db():
    conn = psycopg2.connect(
        dbname=db_settings.DB_NAME,
        user=db_settings.DB_USER,
        password=db_settings.DB_PASS,
        host=db_settings.DB_HOST,
    )
    conn.autocommit = True
    cur = conn.cursor()

    try:
        cur.execute(f"DROP DATABASE IF EXISTS {test_db_settings.DB_NAME} WITH (FORCE)")
    finally:
        cur.close()
        conn.close()


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    create_test_db()
    yield
    drop_test_db()


@pytest.fixture(scope="session", autouse=True)
def populate_test_db(setup_test_db):
    # Use synchronous engine for schema creation
    sync_engine = create_engine(test_db_settings.DB_URL.replace("+asyncpg", "+psycopg2"), echo=True)
    # Create tables synchronously
    Author.metadata.create_all(sync_engine)
    yield

    # Drop tables after the test session
    Author.metadata.drop_all(sync_engine)

    # Dispose of the engine
    sync_engine.dispose()


@pytest.fixture()
def test_db_async_engine():
    return create_async_engine(url=test_db_settings.DB_URL, echo=True)


# Async session factory remains the same for async tests
@pytest.fixture
def async_session_factory(test_db_async_engine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        bind=test_db_async_engine, class_=AsyncSession, expire_on_commit=False
    )


# Fake UnitOfWork remains the same
@pytest.fixture
def fake_uow(async_session_factory):
    return FakeUnitOfWork(async_session_factory)
