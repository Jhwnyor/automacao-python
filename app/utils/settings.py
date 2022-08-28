from dotenv import find_dotenv
from pydantic import BaseSettings, Field


class GlobalSettings(BaseSettings):

    SITE: str = Field(..., env='SITE')

    class Config:
        env_file: str = find_dotenv('.env')


class InputsSettings(BaseSettings):

    EMAIL: str = Field(..., env='EMAIL')
    # Criar o da senha

    class Config:
        env_file: str = find_dotenv('.env')


settings = GlobalSettings()
settings_input = InputsSettings()
