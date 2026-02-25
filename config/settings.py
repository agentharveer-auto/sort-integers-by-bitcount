from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Sort Integers by BitCount"
    debug: bool = False


settings = Settings()
