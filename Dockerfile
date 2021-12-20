FROM python:3.9.9-slim

WORKDIR /app

COPY ./api.py /app
COPY ./questiongenerator.py /app
COPY ./requirements.txt /app

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python","api.py"]