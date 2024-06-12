from abc import ABC, abstractmethod
from typing import Any


class AbstractRepositoryAsync(ABC):
    @abstractmethod
    async def get_one(self, id: Any):
        raise NotImplementedError

    @abstractmethod
    async def get_many(self, **filters):
        raise NotImplementedError

    @abstractmethod
    async def create(self, record: Any):
        raise NotImplementedError

    @abstractmethod
    async def update(self, record: Any):
        raise NotImplementedError

    async def delete(self, id: Any):
        raise NotImplementedError
