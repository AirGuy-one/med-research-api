FROM python:3.13

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    apt-get purge -y curl && apt-get clean

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false &&  \
    poetry install --no-root

COPY . .

CMD ["python", "main.py"]
