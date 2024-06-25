from typing import Optional

from dto.genres import GenreAddDTO, GenreGetDTO
from services.generic_uow_service import GenericUOWService


class GenresService(GenericUOWService):
    async def get(self, id: int) -> GenreGetDTO | None:
        async with self._uow as uow:
            genre = await uow.genres.get_one(id)
            return GenreGetDTO.from_orm(genre) if genre else None

    async def add(self, genre: GenreAddDTO) -> int:
        async with self._uow as uow:
            genre_dict = genre.model_dump()
            genre_model = await uow.genres.create(genre_dict)
            await uow.commit()
            return genre_model.id

    async def search_by_name(self, name: str) -> Optional[int]:
        async with self._uow as uow:
            genre = await uow.genres.get_one_by_filters(name=name)

            return genre.id if genre else None
