import pytest
import pytest_asyncio

from data.db.models.author import Author
from data.db.models.book import Book
from data.db.models.genre import Genre
from data.db.models.user import User


@pytest_asyncio.fixture(autouse=True, scope="package")
async def populate_test_db(async_session_factory):
    async with async_session_factory() as session:
        authors = [
            Author(first_name="Author1", last_name="Author1"),
            Author(first_name="Author2", last_name="Author2"),
        ]
        genres = [Genre(name="Genre1"), Genre(name="Genre2")]
        books = [
            Book(
                title="Book1",
                year=2000,
                description="Desc1",
                authors=[authors[0]],
                genres=genres[0:1],
            ),
            Book(
                title="Book2",
                year=2001,
                description="Desc2",
                authors=authors[0:1],
                genres=[genres[1]],
            ),
        ]
        users = [
            User(name="User1", telegram_id="123", email="user1@example.com"),
            User(name="User2", telegram_id="456", email="user2@example.com"),
        ]

        session.add_all(authors)
        session.add_all(genres)
        session.add_all(books)
        session.add_all(users)
        await session.commit()
