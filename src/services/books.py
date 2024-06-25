from db.models import BookGenres, BookAuthors
from dto.books import BookCreateDTO
from services.generic_uow_service import GenericUOWService


class BooksService(GenericUOWService):
    async def get(self, id: int):
        async with self._uow:
            return await self._uow.books.get_one(id)

    async def add(self, book: BookCreateDTO):
        async with self._uow as uow:
            book_dict = book.model_dump(exclude={"author_ids", "genre_ids"})
            book_model = await uow.books.create(book_dict)
            authors = [await uow.authors.get_one(pk) for pk in book.author_ids]
            genres = [await uow.genres.get_one(pk) for pk in book.genre_ids]

            book_model.authors.extend(authors)
            book_model.genres.extend(genres)
            await self._uow.commit()

            return book_model
