from typing import List, Optional

from sqlalchemy.orm import Mapped, relationship

from data.db.models.base import Base


class Author(Base):
    __tablename__ = "authors"
    first_name: Mapped[str]
    middle_name: Mapped[Optional[str]]
    last_name: Mapped[str]

    books: Mapped[List["Book"]] = relationship(
        back_populates="authors",
        secondary="book_authors",
        lazy="selectin",
    )

    requests: Mapped[Optional[List["Request"]]] = relationship(
        back_populates="authors",
        secondary="request_authors",
        lazy="selectin",
    )
