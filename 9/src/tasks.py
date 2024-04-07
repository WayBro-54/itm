import pytesseract
from celery import Celery
from PIL import Image

from src.config import BASE_DIR, settings


celery = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672')
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
