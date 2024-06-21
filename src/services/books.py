from db.models import Author, Genre, Book
from schemas.books import BookAddSchema
from services.generic_uow_service import GenericUOWService


class BooksService(GenericUOWService):
    async def get_book_by_id(self, id: int):
        async with self._uow:
            return await self._uow.books.get_one(id)

    async def add_book(self, book: BookAddSchema):
        async with self._uow:
            if await self._uow.books.get_one_by_filters(title=book.title):
                return None
            authors = []
            genres = []

            for schema_author in book.authors:
                schema_author_dict = schema_author.model_dump()
                author = await self._uow.authors.get_one_by_filters(
                    **schema_author_dict
                )
                if not author:
                    author = await self._uow.authors.create(
                        Author(**schema_author_dict)
                    )
                authors.append(author)

            for schema_genre in book.genres:
                genre = await self._uow.genres.get_one_by_filters(name=schema_genre)
                if not genre:
                    genre = await self._uow.genres.create(Genre(name=schema_genre))
                genres.append(genre)

            book_model = Book(
                title=book.title, description=book.description, year=book.year
            )
            book_model.authors = authors
            book_model.genres = genres
            book_model = await self._uow.books.create(book_model)
            await self._uow.commit()

            return book_model
