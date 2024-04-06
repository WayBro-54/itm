from datetime import datetime
from typing import Annotated
from fastapi import UploadFile, File
from pydantic import BaseModel


class ImageModelDB(BaseModel):
    id: int
    psth: str
    date: datetime


class TextModelDB(BaseModel):
    id_doc: int
    text: str
