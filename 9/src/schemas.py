from datetime import datetime
from typing import Annotated
from fastapi import Path, HTTPException, status
from pydantic import BaseModel, field_validator


class Test(BaseModel):
    id: int = Path()

    @field_validator('id')
    @classmethod
    def validate(cls, value):
        validate = True if value % 2 == 1 else False
        if not validate:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='id maybe only odd number'
            )
        return value


class ImageModelDB(BaseModel):
    id: int
    psth: str
    date: datetime


class TextModelDB(BaseModel):
    id_doc: int
    text: str
