FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFRED 1
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /code/