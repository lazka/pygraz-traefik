FROM python:3.9-buster as base

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install "poetry==1.1.11"

FROM base AS development

ENV PYTHONDONTWRITEBYTECODE 1
COPY . /app
WORKDIR /app
RUN poetry install

ENTRYPOINT ["poetry", "run", "uvicorn", "--reload", "--host", "0.0.0.0", "--port", "80", "pygraz.main:app"]
EXPOSE 80

FROM base AS production

COPY . /app
WORKDIR /app
RUN poetry install --no-dev

ENTRYPOINT ["poetry", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80", "pygraz.main:app"]
EXPOSE 80
