import pytest
import pytest_asyncio
from application.services import AuthorsService
from api.dto.authors import AuthorAddDTO, AuthorsSearchDTO


@pytest_asyncio.fixture()
def authors_fake_service(fake_uow) -> AuthorsService:
    return AuthorsService(fake_uow)


@pytest.mark.asyncio(loop_scope="session")
async def test_get_author(authors_fake_service: AuthorsService):
    author_dto = await authors_fake_service.get(2)

    # Assertions to validate the result
    assert author_dto is not None
    assert author_dto.id == 2
    assert author_dto.first_name == "Author2"
    assert author_dto.last_name == "Author2"


@pytest.mark.asyncio(loop_scope="session")
async def test_add_author(authors_fake_service: AuthorsService):
    author_add_dto = AuthorAddDTO(first_name="Author3", last_name="Author3", middle_name="GigaChad")

    author_id = await authors_fake_service.add(author_add_dto)

    assert author_id == 3


@pytest.mark.asyncio(loop_scope="session")
async def test_search_by_names(authors_fake_service: AuthorsService):
    search_schema = AuthorsSearchDTO(
        first_name="Author1",
        last_name="Author1",
    )
    author_dtos = await authors_fake_service.search_by_names(search_schema)
    assert len(author_dtos) == 1


@pytest.mark.asyncio(loop_scope="session")
async def test_search_by_names_empty(authors_fake_service: AuthorsService):
    search_schema = AuthorsSearchDTO(first_name="Игорь")
    author_dtos = await authors_fake_service.search_by_names(search_schema)
    assert len(author_dtos) == 0
