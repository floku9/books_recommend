from abc import ABC, abstractmethod
from typing import Any


from repositories.abstract_repository import AbstractRepositoryAsync


class SQLBaseRepositoryAsync(AbstractRepositoryAsync, ABC):
    @abstractmethod
    async def get_one(self, id: int):
        raise NotImplementedError

    @abstractmethod
    async def get_many(self, **filters: dict[str, Any]):
        raise NotImplementedError

    @abstractmethod
    async def create(self, data: dict[str, Any]):
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: int, data: dict[str, Any]):
        raise NotImplementedError

    async def delete(self, id: int):
        raise NotImplementedError
