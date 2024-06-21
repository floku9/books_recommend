from typing import Optional

from pydantic import BaseModel, Field


class AuthorAddSchema(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    middle_name: str | None = Field(max_length=100, default=None)
    last_name: str = Field(min_length=1, max_length=100)
