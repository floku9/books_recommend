import pytest
from application.services import AuthorsService
from data.db.models.author import Author
from tests.conftest import FakeUnitOfWork


@pytest.mark.asyncio
async def test_get_author(fake_uow: FakeUnitOfWork, async_session_factory):
    async with async_session_factory() as session:
        author = Author(first_name="Test", last_name="Author")
        session.add(author)
        await session.commit()

    authors_service = AuthorsService(fake_uow)

    author_dto = await authors_service.get(author.id)

    # Assertions to validate the result
    assert author_dto is not None
    assert author_dto.id == author.id
    assert author_dto.first_name == author.first_name
    assert author_dto.last_name == author.last_name
