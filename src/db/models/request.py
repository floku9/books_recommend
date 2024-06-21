from enum import Enum
from typing import Optional, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from db.models.base import Base, BaseWithCreation


class RequestStatus(Enum):
    NEW = "new"
    PENDING = "pending"
    DONE = "approved"
    ERROR = "error"


class Request(BaseWithCreation):
    __tablename__ = "requests"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship()

    genres: Mapped[Optional[List["Genre"]]] = relationship(
        back_populates="requests",
        secondary="request_genres",
        lazy="selectin",
    )

    authors: Mapped[Optional[List["Author"]]] = relationship(
        back_populates="requests",
        secondary="request_authors",
        lazy="selectin",
    )
    status: Mapped[RequestStatus] = mapped_column(default=RequestStatus.NEW)

    recommendations: Mapped[Optional[List["Recommendation"]]] = relationship(
        back_populates="request", cascade="all"
    )


class RequestGenres(Base):
    __tablename__ = "request_genres"
    request_id = mapped_column(ForeignKey("requests.id"), primary_key=True)
    genre_id = mapped_column(ForeignKey("genres.id"), primary_key=True)


class RequestAuthors(Base):
    __tablename__ = "request_authors"
    request_id = mapped_column(ForeignKey("requests.id"), primary_key=True)
    author_id = mapped_column(ForeignKey("authors.id"), primary_key=True)
