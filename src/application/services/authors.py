from typing import List

from api.dto.authors import AuthorAddDTO, AuthorsSearchDTO, AuthorGetDTO
from application.services.generic_uow_service import GenericUOWService


class AuthorsService(GenericUOWService):

    async def get(self, id: int) -> AuthorGetDTO | None:
        async with self._uow:
            author = await self._uow.authors.get_one(id)
            return AuthorGetDTO.model_validate(author) if author else None

    async def add(self, author: AuthorAddDTO) -> int:
        async with self._uow:
            author_dict = author.model_dump()
            author_model = await self._uow.authors.create(author_dict)
            await self._uow.commit()
            return author_model.id

    async def search_by_names(self, search_schema: AuthorsSearchDTO) -> List[AuthorGetDTO]:
        async with self._uow:
            filters = search_schema.model_dump(exclude_none=True)
            authors = await self._uow.authors.get_many(**filters)

            if authors:
                return [AuthorGetDTO.model_validate(author) for author in authors]
            else:
                return []
