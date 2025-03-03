# Use official Python image as base
FROM python:3.10-slim

# Set environment variables for better performance and logging
ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Set working directory
WORKDIR /app

# Install system dependencies and Poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --no-cache-dir poetry \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files first to leverage Docker caching
COPY pyproject.toml poetry.lock /app/

# Install dependencies without dev dependencies for production
RUN poetry install --no-root --without dev

# Copy application files
COPY app /app/app
COPY tests /app/tests
COPY README.md /app/README.md

# Ensure logs directory exists and set appropriate permissions
RUN mkdir -p /app/logs && chmod -R 777 /app/logs

# Expose FastAPI port
EXPOSE 8000

# Command to run FastAPI server
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
