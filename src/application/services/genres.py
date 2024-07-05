from typing import Optional

from api.dto.genres import GenreAddDTO, GenreGetDTO
from application.services.generic_uow_service import GenericUOWService


class GenresService(GenericUOWService):
    async def get(self, id: int) -> GenreGetDTO | None:
        async with self._uow:
            genre = await self._uow.genres.get_one(id)
            return GenreGetDTO.model_validate(genre) if genre else None

    async def add(self, genre: GenreAddDTO) -> int:
        async with self._uow:
            genre_dict = genre.model_dump()
            genre_model = await self._uow.genres.create(genre_dict)
            await self._uow.commit()
            return genre_model.id

    async def search_by_name(self, name: str) -> Optional[int]:
        async with self._uow as self._uow:
            genre = await self._uow.genres.get_one_by_filters(name=name)

            return genre.id if genre else None
