import asyncio
import dataclasses
from typing import Optional, List

from api.dto.authors import AuthorAddDTO
from application.interactors.gpt.sber.settings import sber_auth_settings


@dataclasses.dataclass
class BookAddUserDTO:
    title: str
    description: Optional[str]
    authors: List[AuthorAddDTO]
    genres: List[str]
    year: int


async def main():
    print(sber_auth_settings)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
