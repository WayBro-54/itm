from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    db_url: str = ''
    title: str = 'File upload'
    tesseract_conf: str = r'--oem 3 --psm 6'

    class Config:
        env_file = f'{BASE_DIR}/.env'


settings = Settings()
