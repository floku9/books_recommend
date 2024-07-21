import os

from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class SBERAuthSettings(BaseSettings):
    AUTHORIZATION_URL: str
    SECRET: str
    AUTHS: str
    SCOPE: str

    model_config = SettingsConfigDict(env_file=find_dotenv(".env"), env_prefix="SBER_", extra="ignore")

class SBERBaseSettings(BaseSettings):
    BASE_URL: str
    model_config = SettingsConfigDict(env_file=find_dotenv(".env"), env_prefix="SBER_", extra="ignore")


sber_auth_settings = SBERAuthSettings()
sber_base_settings = SBERBaseSettings()
