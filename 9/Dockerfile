FROM python:3.10-alpine

WORKDIR  ./app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--reload", "--bild=0.0.0.0:8000"]