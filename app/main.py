import uuid
import asyncio
import logging
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html

# Configure logging with timestamps
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("logs/app.log"),  # Store logs in logs/app.log
        logging.StreamHandler()  # Also log to console
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="UUID Generator API",
    description="A FastAPI server that generates UUIDs",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    """Redirect root endpoint to Swagger UI."""
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API Documentation")

@app.get("/uuid", response_model=dict, status_code=200, summary="Generate a UUID")
def generate_uuid():
    """Generate a unique version 4 UUID."""
    try:
        start_time = datetime.now(timezone.utc)
        unique_id = str(uuid.uuid4())
        end_time = datetime.now(timezone.utc)
        time_difference = round((end_time - start_time).total_seconds(), 6)

        logger.info(
            f"Generated UUID: {unique_id} | Time Taken: {time_difference}s",
            extra={"status": 200}
        )

        return {
            "uuid": unique_id,
            "start_time": start_time.isoformat() + 'Z',
            "end_time": end_time.isoformat() + 'Z',
            "execution_time_seconds": time_difference
        }
    except Exception as e:
        status_code = 500
        error_message = f"Error generating UUID: {str(e)}"
        logger.error(
            error_message,
            extra={"status": status_code}
        )
        raise HTTPException(status_code=status_code, detail=error_message)

@app.get("/async-uuid", response_model=dict, status_code=200, summary="Generate a UUID asynchronously")
async def generate_async_uuid():
    """Generate a unique version 4 UUID asynchronously with a minimum delay of 3 seconds."""
    try:
        start_time = datetime.now(timezone.utc)
        await asyncio.sleep(3)  # Non-blocking delay
        unique_id = str(uuid.uuid4())
        end_time = datetime.now(timezone.utc)
        time_difference = round((end_time - start_time).total_seconds(), 6)

        logger.info(
            f"Generated Async UUID: {unique_id} | Time Taken: {time_difference}s",
            extra={"status": 200}
        )

        return {
            "uuid": unique_id,
            "start_time": start_time.isoformat() + 'Z',
            "end_time": end_time.isoformat() + 'Z',
            "execution_time_seconds": time_difference
        }
    except Exception as e:
        status_code = 500
        error_message = f"Error generating async UUID: {str(e)}"
        logger.error(
            error_message,
            extra={"status": status_code}
        )
        raise HTTPException(status_code=status_code, detail=error_message)
