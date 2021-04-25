# https://github.com/tiangolo/fastapi/issues/2336#issuecomment-724906602

from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_user: str = ""
    postgres_password: str = ""
    postgres_host: str = ""
    postgres_db: str = ""

    class Config:
        env_file = ".env"


settings = Settings()


@lru_cache()
def get_settings():
    return settings


# To use: get_settings().postgres_user
