from api.dto.books import BookCreateDTO, BookGetDTO
from application.services.generic_uow_service import GenericUOWService


class BooksService(GenericUOWService):
    async def get(self, id: int) -> BookGetDTO | None:
        async with self._uow:
            book = await self._uow.books.get_one(id)
            return BookGetDTO.model_validate(book) if book else None

    async def add(self, book: BookCreateDTO) -> int:
        async with self._uow:
            book_dict = book.model_dump(exclude={"author_ids", "genre_ids"})
            book_model = await self._uow.books.create(book_dict)
            authors = [await self._uow.authors.get_one(id=id) for id in book.author_ids]
            genres = [await self._uow.genres.get_one(id=id) for id in book.genre_ids]

            book_model.authors.extend(authors)
            book_model.genres.extend(genres)
            await self._uow.commit()

            return book_model.id
