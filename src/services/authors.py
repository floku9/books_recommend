from typing import List

from dto.authors import AuthorAddDTO, AuthorsSearchDTO, AuthorGetDTO
from services.generic_uow_service import GenericUOWService


class AuthorsService(GenericUOWService):

    async def get(self, id: int) -> AuthorGetDTO | None:
        async with self._uow:
            author = await self._uow.authors.get_one(id)
            if author:
                return AuthorGetDTO.from_orm(author)
            else:
                return None

    async def add(self, author: AuthorAddDTO) -> int:
        async with self._uow as uow:
            author_dict = author.model_dump()
            author_model = await uow.authors.create(author_dict)
            await uow.commit()
            return author_model.id

    async def search_by_names(
        self, search_schema: AuthorsSearchDTO
    ) -> List[AuthorGetDTO] | None:
        async with self._uow:
            authors = await self._uow.authors.get_many(
                **search_schema.model_dump(exclude_none=True)
            )
            if authors:
                return [AuthorGetDTO.from_orm(author) for author in authors]
            else:
                return None
