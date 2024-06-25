from typing import Optional
from dto.base import BaseDTO
from utils.custom_types import NameField, NameDefaultField


class AuthorAddDTO(BaseDTO):
    first_name: str = NameField
    middle_name: str | None = NameDefaultField
    last_name: str = NameField


class AuthorsSearchDTO(BaseDTO):
    first_name: Optional[str] = NameDefaultField
    middle_name: Optional[str] = NameDefaultField
    last_name: Optional[str] = NameDefaultField


class AuthorGetDTO(BaseDTO):
    id: int
