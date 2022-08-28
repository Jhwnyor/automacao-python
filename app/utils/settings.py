from dotenv import find_dotenv
from pydantic import BaseSettings, Field


class GlobalSettings(BaseSettings):

    SITE: str = Field(..., env='SITE')
    EMAIL: str = Field(..., env='EMAIL')
    SENHA: str = Field(..., env='SENHA')


    class Config:
        env_file: str = find_dotenv('.env')


class InputsSettings(BaseSettings):

    INPUT_EMAIL: str = Field(..., env='INPUT_EMAIL')
    INPUT_SENHA: str = Field(..., env='INPUT_SENHA')

    class Config:
        env_file: str = find_dotenv('.env')


class ButtonSettings(BaseSettings):
    BUTTON_LOGIN: str = Field(..., env='BUTTON_LOGIN')

    class Config:
        env_file: str = find_dotenv('.env')


settings = GlobalSettings()
settings_input = InputsSettings()
settings_button = ButtonSettings()
