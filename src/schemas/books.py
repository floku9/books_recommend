from typing import List, Optional

from pydantic import BaseModel, Field

from schemas.authors import AuthorAddSchema


class BookAddUserSchema(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(max_length=1000)
    authors: List[AuthorAddSchema]
    genres: Optional[List[str]]
    year: int = Field(ge=0, le=2100)

    class Config:
        orm_mode = True
