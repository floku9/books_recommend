from abc import ABC, abstractmethod
from typing import Any

from aiohttp import ClientSession


class GPTClientAbstract(ABC):
    async def __aenter__(self):
        raise NotImplementedError

    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def get_completion(self, prompt: str, messages: list[str]) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_tokens_count(self, prompt: str, messages: list[str]) -> Any:
        raise NotImplementedError


class HTTPGPTClientAbstract(ABC):

    def __init__(self, async_session: ClientSession):
        self._async_session = async_session

    async def __aenter__(self):
        await self._authorize()

    async def __aexit__(self, *args):
        raise NotImplementedError

    def _authorize(self):
        raise NotImplementedError

    @abstractmethod
    async def get_completion(self, prompt: str, messages: list[str]) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_tokens_count(self, prompt: str, messages: list[str]) -> Any:
        raise NotImplementedError
