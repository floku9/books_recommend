from api.dto.base import BaseDTO
from utils.custom_types import NameField


class GenreAddDTO(BaseDTO):
    name: str = NameField


class GenreGetDTO(GenreAddDTO):
    id: int
