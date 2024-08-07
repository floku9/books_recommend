from data.db.configuration import async_session_factory
from data.repositories.sql.orm.db_models_repositories import (
    AuthorRepository,
    BookRepository,
    GenreRepository,
    RecommendationRepository,
    RequestRepository,
    UserRepository,
)
from data.uow.abstract_uow import AbstractUnitOfWorkAsync


class SQLORMUnitOfWork(AbstractUnitOfWorkAsync):

    def __init__(self):
        self._session_factory = async_session_factory

    async def __aenter__(self):
        self._session = self._session_factory()
        self.authors = AuthorRepository(self._session)
        self.books = BookRepository(self._session)
        self.genres = GenreRepository(self._session)
        self.recommendations = RecommendationRepository(self._session)
        self.requests = RequestRepository(self._session)
        self.users = UserRepository(self._session)
        return self

    async def __aexit__(self, *args):
        await self.rollback()
        await self._session.close()

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
