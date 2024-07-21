import asyncio
import dataclasses
from typing import Optional, List
from api.dto.authors import AuthorsSearchDTO, AuthorAddDTO
from api.dto.books import BookCreateDTO
from api.dto.genres import GenreAddDTO
from application.interactors.gpt.sber.settings import sber_auth_settings
from application.services import AuthorsService
from application.services import BooksService
from application.services import GenresService
from data.uow.sql_orm_uow import SQLORMUnitOfWork

@dataclasses.dataclass
class BookAddUserDTO:
    title: str
    description: Optional[str]
    authors: List[AuthorAddDTO]
    genres: List[str]
    year: int


async def main():
    print(sber_auth_settings)



if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
