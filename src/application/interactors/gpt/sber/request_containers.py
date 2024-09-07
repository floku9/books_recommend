from typing import Optional, List

from dataclasses import dataclass
from uuid import UUID

from pydantic import BaseModel, Field
from enum import Enum


class ModelTypes(str, Enum):
    GIGACHAT_LITE = "GigaChat"
    GIGACHAT_LITE_PLUS = "GigaChat-Plus"
    GIGACHAT_PRO = "GigaChat-Pro"


class Roles(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class Message(BaseModel):
    role: Roles = Field(description="The role of the message sender", default=Roles.USER)
    content: str


class ModelParameters(BaseModel):
    model_type: ModelTypes = Field(
        description="The role of the message sender",
        default=ModelTypes.GIGACHAT_LITE,
        alias="model",
        alias_priority=2,
    )
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    n: Optional[int] = None
    stream: Optional[bool] = None
    max_tokens: Optional[int] = None
    repetition_penalty: Optional[float] = None


class RequestBody(BaseModel):
    model_parameters: ModelParameters
    messages: List[Message]

    def to_request_dict(self):
        data = self.model_dump(by_alias=True)
        # Flatten the model_parameters into the main dict
        parameters = data.pop("model_parameters")
        data.update(parameters)
        return data
