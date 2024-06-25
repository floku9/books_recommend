from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseWithCreation


class Recommendation(BaseWithCreation):
    __tablename__ = "recommendations"

    request_id: Mapped[int] = mapped_column(ForeignKey("requests.id"), nullable=False)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    rating: Mapped[float]
    gpt_description: Mapped[str]

    request: Mapped["Request"] = relationship(back_populates="recommendations")
    book: Mapped["Book"] = relationship()
