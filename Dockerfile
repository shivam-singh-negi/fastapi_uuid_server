# Use official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy project files
COPY pyproject.toml poetry.lock /app/

# Install dependencies (excluding dev dependencies)
RUN poetry install --no-root --without dev

# Copy application files
COPY . /app/

# Expose FastAPI port
EXPOSE 9090

# Run FastAPI server
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9090"]
