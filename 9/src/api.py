from typing import Annotated
from fastapi import APIRouter, File, UploadFile, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas import ImageModelDB, TextModelDB, Test
from src.crud import crud_document, crud_document_text
from src.db import get_async_session
from src.tasks import task_analyse_document

router = APIRouter()


@router.get('/test/{id}')
async def test_chet(
        id: Test = Depends(),
        # id: Annotated[int, Path(pattern=r'[13579]$')]
):
    return id


@router.post('/upload_doc')
async def give_image(
        image: UploadFile = File(),
        session: AsyncSession = Depends(get_async_session),
):
    res = await crud_document.create(image, session)
    return res


@router.post(
    '/doc_analyse/{id_img}',
    response_model=TextModelDB,
    response_model_exclude_none=True,
)
async def analysis_text_to_img(
        id_img: int,
        session: AsyncSession = Depends(get_async_session),
):
    """
    This enpoint make background task - analysis to upload file,
    exchange text to file in string,
    and save in model "DocumentText"

    :param session:
    :param id_img: id documents to upload id path "/upload_doc"

    :return: "Done"
    """
    obj_db = await crud_document.get_item(id_img, session)
    if not obj_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Could not find',
        )

    get_text_image = task_analyse_document.delay(obj_db.psth)
    get_text_image = get_text_image.get(timeout=1000)

    result = await crud_document_text.save_text_analysis(
        obj_db.id,
        get_text_image,
        session,
    )
    return result


@router.get(
    '/get_text/{id_img}',
    response_model=TextModelDB)
async def get_text_analysis(
    id_img: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    This enpoint return the text analysis given the id img.

    :param id_img: This ID the image in table Documents
    :param session:
    :return:
    """
    obj_db = await crud_document_text.get_image_text(id_img, session)
    if not obj_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Could not find',
        )
    return obj_db


@router.delete(
    '/doc_delete/{id_img}',
    response_model=ImageModelDB,
)
async def doc_delete(
        id_img: int,
        session: AsyncSession = Depends(get_async_session),
):
    """
    This method deletes an image and text from the database
    :param id_img:
    """
    obj_db = await crud_document.get_item(id_img, session)
    if not obj_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Could not find',
        )
    res = await crud_document.remove(obj_db, session)
    return res
