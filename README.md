# 🚀 FastAPI UUID Generator

## 📚 Overview

FastAPI UUID Generator is a lightweight, high-performance API service built using **FastAPI**. It provides endpoints to generate **universally unique identifiers (UUIDs)**, including an asynchronous version that introduces a **non-blocking delay of 3 seconds**.

This service is useful for applications that require UUIDs for **session management, unique identifiers, or distributed systems**.

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

## 🫠 Installation & Running Locally

### **1️⃣ Install Poetry (If Not Installed)**  

This project uses [Poetry](https://python-poetry.org/) for dependency management. If you haven't installed it, run:  

```bash
pip install poetry
```

### **2️⃣ Clone the Repository**  

```bash
git clone <your-repo-url>
cd fastapi-service
```

### **3️⃣ Install Dependencies**  

```bash
poetry install
```

### **4️⃣ Run the FastAPI Server**  

```bash
poetry run uvicorn app.main:app --reload
```

The server will be available at **[http://127.0.0.1:9090](http://127.0.0.1:9090)**  

---  

## 🧪 Running Tests  

To verify that everything is working correctly, run:  

```bash
poetry run pytest
```

This will execute all unit tests defined in the **tests/** directory, including tests for **error handling**.  

---  

## 🐛 API Documentation  

FastAPI provides **interactive API documentation**. Once the server is running, access:  

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

Swagger UI will open **by default** when accessing `/`.  

---  

## 🐋 Running with Docker  

If you prefer running the service in a **Docker container**, follow these steps:  

### **1️⃣ Build the Docker Image**  

```bash
docker build -t fastapi-uuid .
```

### **2️⃣ Run the Container**  

```bash
docker run -p 8000:8000 fastapi-uuid
```

This exposes the API at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**  

### **3️⃣ Running Tests in Docker**  

To execute tests inside the container:  

```bash
docker run fastapi-uuid poetry run pytest
```

---  

## 🌟 API Endpoints  

| Method  | Endpoint      | Description                                   | Status Code |
| ------- | ------------- | --------------------------------------------- | ----------- |
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
- **Logs are stored** in a dedicated `logs/app.log` file.  
- If the log file doesn't exist, **it is created dynamically**.  

In case of failure, the API responds with **500 Internal Server Error**.  

---  

## 🛠 Project Structure  

```
fastapi-service/
│── app/
│   ├── main.py         # FastAPI application
│── tests/
│   ├── test_main.py    # Unit tests (including error handling tests)
│── Dockerfile          # Docker setup
│── pyproject.toml      # Dependencies and package management
│── README.md           # Documentation
│── logs/               # Stores log files (if configured)
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

## 🐜 License  

This project is licensed under the **MIT License**.  

---  

🚀 **Enjoy coding! If you have any questions, feel free to reach out.**

