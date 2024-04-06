import pytesseract
from celery import Celery
from PIL import Image

from src.config import BASE_DIR, settings
from src.crud import crud_document_text

celery = Celery('tasks', broker=f'amqp://guest:guest@0.0.0.0:5672')
celery.conf.broker_connection_retry_on_startup = True
celery.conf.result_backend = 'rpc://'
celery.conf.task_serializer = 'json'
celery.conf.result_serializer = 'json'
celery.conf.accept_content = ['json']

@celery.task
def task_analyse_document(filename) -> str:
    img = Image.open(f'{BASE_DIR}/documents/{filename}')
    text = pytesseract.image_to_string(
        img,
        lang='rus',
        config=settings.tesseract_conf,
    )
    return text
    # crud_document_text.save_text_analysis(obj_db.id, text, session)
