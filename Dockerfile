FROM python:3.11

RUN pip install --upgrade pip  \
    && pip install "poetry==1.6.1"  \
    && poetry config virtualenvs.create false

WORKDIR /api_movie_app

COPY ["poetry.lock", "pyproject.toml", "./"]

RUN poetry install --no-root --no-interaction --without dev

WORKDIR /app

COPY app .

WORKDIR ..

EXPOSE 8001

CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]

