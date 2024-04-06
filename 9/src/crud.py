import shutil
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import BASE_DIR
from src.models import Documents, DocumentText


class CRUD:

    def __init__(
        self,
        model,
    ):
        self.model = model

    async def get_item(
        self,
        id_obj: int,
        session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(
                self.model
            ).where(
                self.model.id == id_obj
            )
        )
        return db_obj.scalar_one_or_none()

    async def remove(
        self,
        obj_db,
        session: AsyncSession,
    ):
        await session.delete(obj_db)
        await session.commit()
        return obj_db


class DocumentCRUD(CRUD):

    async def create(
            self,
            obj_in,
            session: AsyncSession,
    ):
        save_path = f'{BASE_DIR}/documents/{obj_in.filename}'

        with open(save_path, 'wb') as buffer:
            shutil.copyfileobj(obj_in.file, buffer)

        # добавляем в Document
        obj_db = self.model(
            psth=obj_in.filename,
            date=datetime.now(),
        )

        session.add(obj_db)
        await session.commit()

        return obj_db


class TextDocumentCRUD(CRUD):

    async def save_text_analysis(
            self,
            id_img: int,
            text: str,
            session: AsyncSession,
    ):
        obj_db = self.model(
            id_doc=id_img,
            text=text,
        )
        session.add(obj_db)
        await session.commit()

        return obj_db

    async def get_image_text(
        self,
        id_obj: int,
        session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(
                self.model
            ).where(
                self.model.id_doc == id_obj
            )
        )
        return db_obj.scalar_one_or_none()


crud_document = DocumentCRUD(Documents)
crud_document_text = TextDocumentCRUD(DocumentText)
