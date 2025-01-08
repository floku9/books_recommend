import uuid
from typing import Any
from urllib.parse import urljoin

from aiohttp import ClientSession

from utils.exceptions import HTTPExceptionsFactory
from ..gpt_client_abstract import HTTPGPTClientAbstract
from .settings import sber_auth_settings, sber_base_settings
from .request_containers import ModelParameters, RequestBody


class SBERGPTClient(HTTPGPTClientAbstract):
    _auth_settings = sber_auth_settings
    _base_settings = sber_base_settings

    def __init__(self, async_session: ClientSession, model_parameters: ModelParameters):
        self._model_parameters = model_parameters
        super().__init__(async_session=async_session)

    async def __aenter__(self):
        await super().__aenter__()
        return self

    async def __aexit__(self, *args): ...

    async def _authorize(self):
        query = "/api/v2/oauth"
        url = urljoin(self._auth_settings.AUTHORIZATION_URL, query)
        params = self._auth_settings.SCOPE

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "RqUID": str(uuid.uuid4()),
            "Authorization": f"Basic {self._auth_settings.AUTHS}",
        }

        async with self._async_session.post(
            url,
            headers=headers,
            data=params,
            timeout=20,
        ) as response:
            if response.status != 200:
                HTTPExceptionsFactory.raise_exception(
                    status_code=response.status, reason=response.reason
                )
            json_response = await response.json()
            self._auth_token = json_response["access_token"]

    async def get_completion(self, prompt: str, messages: list[str]) -> str:

        query = "/api/v1/chat/completions"

        url = urljoin(self._base_settings.BASE_URL, query)

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self._auth_token}",
        }

        params = RequestBody(
            model_parameters=self._model_parameters,
            messages=[
                {"role": "system", "content": prompt},
                *[{"role": "user", "content": message} for message in messages],
            ],
        )

        async with self._async_session.post(
            url=url,
            headers=headers,
            json=params.to_request_dict(),
            timeout=30,
        ) as response:
            if response.status != 200:
                HTTPExceptionsFactory.raise_exception(
                    status_code=response.status, reason=response.reason
                )
            json_response = await response.json()
            
            return json_response["choices"][0]["message"]["content"]

    async def get_tokens_count(self, prompt: str, messages: list[str]) -> Any: ...
