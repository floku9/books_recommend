from typing import List, Optional

from pydantic import Field

from dto.base import BaseDTO
from utils.custom_types import NameField, YearField


class BookCreateDTO(BaseDTO):
    title: str = NameField
    description: Optional[str] = Field(max_length=1000)
    year: int = YearField
    genre_ids: List[int] = Field(min_items=1)
    author_ids: List[int] = Field(min_items=1)
