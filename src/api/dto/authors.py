from typing import Optional
from api.dto.base import BaseDTO
from utils.custom_types import NameField, NameDefaultField


class AuthorAddDTO(BaseDTO):
    first_name: str = NameField
    middle_name: str | None = NameDefaultField
    last_name: str = NameField


class AuthorsSearchDTO(BaseDTO):
    first_name: str = NameField
    middle_name: Optional[str] = NameDefaultField
    last_name: Optional[str] = NameDefaultField


class AuthorGetDTO(BaseDTO):
    id: int
    first_name: str
    middle_name: Optional[str]
    last_name: str
