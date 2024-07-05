from abc import ABC, abstractmethod


class GPTClientAbstract(ABC):
    @abstractmethod
    async def generate_text(self, text: str) -> str:
        raise NotImplementedError