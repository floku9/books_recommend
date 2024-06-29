from typing import Type, TypeVar

from pydantic import BaseModel

from repositories.sql.sql_base_repository import SQLBaseRepositoryAsync
from uow.sql_orm_uow import SQLORMUnitOfWork

DTO = TypeVar("DTO", bound=BaseModel)


class GenericUOWService:
    def __init__(self, uow: SQLORMUnitOfWork):
        self._uow = uow


class MixinBase[DTO]:
    dto: Type[DTO] = None
    repository: Type[SQLBaseRepositoryAsync] = None


class GetMixin[DTO](MixinBase[DTO]):
    async def get(self, id: int) -> DTO | None:
        model = await self.repository.get_one(id=id)

        return self.dto.from_orm(model) if model else None
