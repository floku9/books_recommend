from typing import Protocol, TypeVar

from api.dto.base import BaseDTO
from data.uow.sql_orm_uow import SQLORMUnitOfWork

DTO = TypeVar("DTO", bound=BaseDTO)


class Get(Protocol):
    async def get(self, id: int) -> BaseDTO:
        raise NotImplementedError


class Add(Protocol):
    async def add(self, dto: BaseDTO) -> int:
        raise NotImplementedError


class GenericUOWService(Get, Add):
    def __init__(self, uow: SQLORMUnitOfWork):
        self._uow = uow
