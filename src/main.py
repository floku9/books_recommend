import asyncio

from db.configuration import async_session_factory
from schemas.books import BookAddSchema
from services.books import BooksService
from uow.sql_orm_uow import SQLORMUnitOfWork


async def main():
    uow = SQLORMUnitOfWork(session_factory=async_session_factory)
    book = BookAddSchema(
        title="1984",
        description="культовый роман Джорджа Оруэлла, действие которого разворачивается в "
                    "тоталитарном, бюрократическом государстве, где процветает пропаганда и цензура, "
                    "а тотальная слежка ведется круглосуточно, и где один человек решил побороться "
                    "за право быть индивидуальной личностью",
        authors=[
            {"first_name": "Джордж", "last_name": "Оруэлл"},
        ],
        genres=["Роман", "Антиутопия"],
        year=1949,
    )
    created_book = await BooksService(uow).add_book(book)
    print(created_book)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
