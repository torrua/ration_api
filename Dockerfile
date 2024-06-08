FROM python:3.12-alpine
WORKDIR /app
COPY ./requirements-docker.txt /app/requirements-docker.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements-docker.txt
COPY ./src /app/src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]