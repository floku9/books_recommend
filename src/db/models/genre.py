from typing import Optional, List

from sqlalchemy.orm import relationship, Mapped

from db.models.base import Base


class Genre(Base):
    __tablename__ = "genres"
    name: Mapped[str]

    books: Mapped[Optional[List["Book"]]] = relationship(
        back_populates='genres',
        secondary='book_genres',
        lazy="selectin",
    )

    requests: Mapped[Optional[List["Request"]]] = relationship(
        back_populates="genres",
        secondary="request_genres",
        lazy="selectin",
    )

