FROM python:3.13-alpine3.22

# Set working directory
WORKDIR /app

COPY . .

RUN pip install -U pip uv && \
    uv sync

ENV PYTHONPATH=/app/

# Set the entrypoint
ENTRYPOINT ["uv", "run", "python", "src/cli/entrypoint.py"]