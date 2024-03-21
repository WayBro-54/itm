from pathlib import Path
from pydantic_settings import BaseSettings

BASEDIR = Path(__file__).parent.parent


class DataBaseSettings(BaseSettings):
    echo: bool = True
    future: bool = True
    url: str = ""

    class Config:
        env_file = f"{BASEDIR}/.env"


class BaseSetting(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()


settings = BaseSetting()
