# 🚀 FastAPI UUID Generator

## 📚 Overview
FastAPI UUID Generator is a high-performance API service built using **FastAPI**. It provides endpoints to generate **universally unique identifiers (UUIDs)**, including an asynchronous version with a **non-blocking delay of 3 seconds**.

This service is useful for applications requiring UUIDs for **session management, unique identifiers, or distributed systems**.

---  

## 📌 Features

✅ **Generate UUIDs instantly**  
✅ **Async UUID generation with a controlled delay**  
✅ **Interactive API documentation** with Swagger and ReDoc  
✅ **Error logging with timestamps & status codes**  
✅ **Docker support** for easy deployment  
✅ **Unit-tested for reliability**  
✅ **Error handling tests included**  

---  

## 📥 Installation

### **1️⃣ Install Poetry (If Not Installed)**  
This project uses [Poetry](https://python-poetry.org/) for dependency management. Install it using:

```bash
pip install poetry
```

### **2️⃣ Clone the Repository**  

```bash
git clone https://github.com/shivam-singh-negi/fastapi_uuid_server.git
cd fastapi_uuid_server
```

### **3️⃣ Install Dependencies**  

```bash
poetry install
```

### **4️⃣ Run the FastAPI Server**  

```bash
poetry run uvicorn app.main:app --reload
```

The server will be available at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**  

---  

## 🧪 Running Tests  

To verify that everything is working correctly, run:  

```bash
poetry run pytest
```

This executes all unit tests in the **tests/** directory, including **error handling tests**.  

---  

## 🐛 API Documentation  

FastAPI provides **interactive API documentation**. After starting the server, access:  

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

---  

## 🐋 Running with Docker  

### **1️⃣ Build the Docker Image**  

```bash
docker build -t fastapi-uuid .
```

### **2️⃣ Run the Container**  

```bash
docker run -p 9090:9090 fastapi-uuid
```

This exposes the API at **[http://127.0.0.1:9090](http://127.0.0.1:9090)**  

### **3️⃣ Running Tests in Docker**  

To execute tests inside the container:  

```bash
docker run fastapi-uuid poetry run pytest
```

---  

## 🌟 API Endpoints  

| Method  | Endpoint      | Description                                   | Status Code |
|---------|-------------|---------------------------------------------|-------------|
| **GET** | `/uuid`       | Returns a unique UUID.                        | 200         |
| **GET** | `/async-uuid` | Returns a unique UUID after a 3-second delay. | 200         |

### **Example Response (`/uuid`)**  

```json
{
  "uuid": "550e8400-e29b-41d4-a716-446655440000",
  "start_time": "2025-03-03T12:30:45Z",
  "end_time": "2025-03-03T12:30:45Z",
  "execution_time_seconds": 0.0001
}
```

### **Example Response (`/async-uuid`)**  

```json
{
  "uuid": "b3f7a486-7a28-4db5-8af2-b0c6f1447c88",
  "start_time": "2025-03-03T12:30:45Z",
  "end_time": "2025-03-03T12:30:48Z",
  "execution_time_seconds": 3.0001
}
```

---  

## 🐝 Error Handling & Logging  

The application logs all errors **with timestamps, status codes, and error details**.  

### Example Log Entry (Stored in `logs/app.log`):  

```
2025-03-03 12:31:00 - ERROR - Status: 500 - Error generating UUID: Internal Server Error
```

### How It Works:  
- **Errors are captured** and logged automatically.  
- **Logs are stored** in `logs/app.log`.  
- If the log file doesn't exist, **it is created dynamically**.  

If an error occurs, the API responds with **500 Internal Server Error**.  

---  

## 🛠 Project Structure  

```
fastapi-service/
│── app/
│   ├── __init__.py      # Package initialization
│   ├── main.py         # FastAPI application
│── tests/
│   ├── __init__.py      # Package initialization
│   ├── test_main.py    # Unit tests (including error handling tests)
│── logs/
│   ├── __init__.py      # Package initialization
│   ├── app.log         # Stores captured logs.
│── .gitignore          # Git ignore file
│── Dockerfile          # Docker setup
│── poetry.lock         # Poetry lock file
│── pyproject.toml      # Dependencies and package management
│── README.md           # Documentation
```

---  

## 🐟 Error Handling Tests  

The test suite includes cases for handling **internal server errors** when UUID generation fails. 

### **Error Handling Test Cases:**
- Simulating UUID generation failure for `/uuid` endpoint
- Simulating UUID generation failure for `/async-uuid` endpoint
- Validating API response with status **500 Internal Server Error**

These tests ensure the application is **resilient to unexpected failures**.  

---  

🚀 **If you have any questions, feel free to reach out.**

