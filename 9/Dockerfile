FROM python:3.10-alpine

WORKDIR  ./app

COPY . .

RUN pip install -r requirements.txt
RUN apk update && apk add --no-cache \
    tesseract-ocr \
    tesseract-ocr-dev \
    tesseract-ocr-data-rus

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
