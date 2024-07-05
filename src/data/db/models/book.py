from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from data.db.models.base import BaseWithCreation, Base


class Book(BaseWithCreation):
    __tablename__ = "books"
    title: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()

    genres: Mapped[List["Genre"]] = relationship(
        back_populates="books",
        secondary="book_genres",
        lazy="selectin",
    )

    authors: Mapped[List["Author"]] = relationship(
        back_populates="books",
        secondary="book_authors",
        lazy="selectin",
    )


class BookAuthors(Base):
    __tablename__ = "book_authors"
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), primary_key=True)


class BookGenres(Base):
    __tablename__ = "book_genres"
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"), primary_key=True)
