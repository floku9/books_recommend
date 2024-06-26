import asyncio
import dataclasses
from typing import Optional, List

from db.configuration import async_session_factory
from dto.authors import AuthorsSearchDTO, AuthorAddDTO
from dto.books import BookCreateDTO
from dto.genres import GenreAddDTO
from services.authors import AuthorsService
from services.books import BooksService
from services.genres import GenresService
from uow.sql_orm_uow import SQLORMUnitOfWork

@dataclasses.dataclass
class BookAddUserDTO:
    title: str
    description: Optional[str]
    authors: List[AuthorAddDTO]
    genres: List[str]
    year: int


async def main():
    uow = SQLORMUnitOfWork(async_session_factory)
    book_schema = BookAddUserDTO(
        title="1984",
        description="культовый роман Джорджа Оруэлла, действие которого разворачивается в "
        "тоталитарном, бюрократическом государстве, где процветает пропаганда и цензура, "
        "а тотальная слежка ведется круглосуточно, и где один человек решил побороться "
        "за право быть индивидуальной личностью",
        authors=[
            AuthorAddDTO(first_name="Джордж", last_name="Оруэлл"),
        ],
        genres=["Кирилл", "Антиутопия"],
        year=1949,
    )

    genres_service = GenresService(uow)
    authors_service = AuthorsService(uow)

    genre_ids, author_ids = [], []

    for genre in book_schema.genres:
        genre_id = await genres_service.search_by_name(genre)
        if not genre_id:
            genre_id = await genres_service.add(GenreAddDTO(name=genre))
        genre_ids.append(genre_id)

    for author in book_schema.authors:
        authors = await authors_service.search_by_names(
            AuthorsSearchDTO(**author.model_dump())
        )
        if not authors:
            author_id = await authors_service.add(author)
        else:
            author_id = authors[0].id
        author_ids.append(author_id)

    book_create_schema = BookCreateDTO(
        title=book_schema.title,
        description=book_schema.description,
        year=book_schema.year,
        genre_ids=genre_ids,
        author_ids=author_ids,
    )
    created_book = await BooksService(uow).add(book_create_schema)
    print(created_book)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
