import asyncio
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from data import db
from data.db.settings import db_settings
from data.uow.sql_orm_uow import SQLORMUnitOfWork
from data.db.models.author import Author  # noqa
from data.db.models.base import Base

# Clone the database settings and set up the test database
test_db_settings = db_settings.model_copy()
test_db_settings.DB_NAME = "test_db"

default_db_settings = db_settings.model_copy()
default_db_settings.DB_NAME = "postgres"


class FakeUnitOfWork(SQLORMUnitOfWork):
    def __init__(self, session_factory):
        self._session_factory = session_factory


async def create_test_db():
    """Create the test database asynchronously."""
    engine = create_async_engine(test_db_settings.DB_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()


async def drop_test_db():
    """Drop the test database asynchronously."""
    engine = create_async_engine(test_db_settings.DB_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_test_db():
    """Setup and teardown for the test database."""
    await create_test_db()
    yield
    await drop_test_db()


@pytest_asyncio.fixture(scope="session")
async def test_db_async_engine():
    """Fixture for creating an async engine."""
    engine = create_async_engine(test_db_settings.DB_URL, echo=True)
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture(scope="session")
async def async_session_factory(test_db_async_engine) -> async_sessionmaker[AsyncSession]:
    """Fixture for creating an async session factory."""
    return async_sessionmaker(
        bind=test_db_async_engine, class_=AsyncSession, expire_on_commit=False
    )


@pytest_asyncio.fixture(scope="session")
async def fake_uow(async_session_factory):
    """Fixture for providing a fake Unit of Work."""
    return FakeUnitOfWork(async_session_factory)