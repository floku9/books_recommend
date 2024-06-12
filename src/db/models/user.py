from typing import List, Optional

from sqlalchemy.orm import Mapped, relationship

from db.models.base import BaseWithCreation


class User(BaseWithCreation):
    __tablename__ = "users"
    name: Mapped[str]
    email: Mapped[str | None]
    telegram_id: Mapped[str]
    requests: Mapped[List["Request"]] = relationship(back_populates="user", lazy="selectin")

