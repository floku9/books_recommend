from fastapi import APIRouter, HTTPException

from api.dependencies import UOWDependency
from api.dto.authors import AuthorGetDTO, AuthorsSearchDTO
from application.services import AuthorsService
from data.uow.sql_orm_uow import SQLORMUnitOfWork

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.get("/{id}", response_model=AuthorGetDTO)
async def get_author(id: int, uow: UOWDependency):
    author = await AuthorsService(uow).get(id=id)  # type: ignore
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.post("/search_by_name", response_model=list[AuthorGetDTO])
async def get_authors(author_search: AuthorsSearchDTO, uow: UOWDependency):
    authors = await AuthorsService(uow).search_by_names(author_search)  # type: ignore
    if not authors:
        raise HTTPException(status_code=404, detail="Authors not found")
    return authors
