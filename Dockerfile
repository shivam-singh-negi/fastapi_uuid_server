# Use official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only pyproject.toml and poetry.lock first (to take advantage of Docker cache)
COPY pyproject.toml poetry.lock /app/

# Install dependencies (including dev dependencies)
RUN poetry install --no-interaction  --no-root

# Now copy the application files (app, tests, logs, etc.)
COPY . /app/

# Expose FastAPI port
EXPOSE 9090

# Run the tests using pytest
RUN poetry run pytest

# Run FastAPI server
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9090"]
