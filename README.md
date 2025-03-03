# 🚀 FastAPI UUID Generator  

## 📚 Overview  
FastAPI UUID Generator is a lightweight API service built using **FastAPI**. It provides endpoints to generate **universally unique identifiers (version 4 UUIDs)**, including an **asynchronous version with a 3-second delay**.  

---

## 📌 Features  

✅ **Generate UUIDs instantly**  
✅ **Async UUID generation with a controlled delay**  
✅ **Interactive API documentation with Swagger**  
✅ **Error logging with timestamps & status codes**  
✅ **Docker support for easy deployment**  
✅ **Unit-tested for reliability**  
✅ **Error handling tests included**  

---  

## 📂 Project Structure  

```
fastapi-uuid-server/
│── app/
│   ├── __init__.py      # Package initialization
│   ├── main.py          # FastAPI application
│── tests/
│   ├── __init__.py      # Package initialization
│   ├── test_main.py     # Unit tests (including error handling tests)
│── logs/
│   ├── __init__.py      # Package initialization
│   ├── app.log          # Stores captured logs
│── .gitignore           # Git ignore file
│── Dockerfile           # Docker setup
│── poetry.lock          # Poetry lock file
│── pyproject.toml       # Dependencies and package management
│── README.md            # Documentation
```

---

## 🧅 Installation & Setup  

### **1️⃣ Install Poetry (If Not Installed)**  
[Poetry](https://python-poetry.org/) is used for dependency management. Install it using:  

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
poetry run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

The server will be available at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**  

---  

## 💜 API Documentation  

FastAPI provides **interactive API documentation**. Once the server is running, access:  

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
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

## 🛡️ Error Handling  

### **Error Logging**  

- All success/errors are **automatically logged** with timestamps, status codes, and details.  
- Logs are stored in:  
  ```
  logs/app.log
  ```

### **Example Log Entry**  
![image](https://github.com/user-attachments/assets/baea2c47-d7f6-408a-b9e8-6d5aba2d2c2b)


### **Error Responses**  

---  

## 🤦‍♂️ Running Tests  

To verify that everything is working correctly, run:  

```bash
poetry run pytest
```

This executes all unit tests in the **tests/** directory, including:  

✅ **UUID Generation Tests**  
✅ **Async UUID Generation Tests**  
✅ **Error Handling Tests**  

---  

## 🐫 Running with Docker  
Ensure that docker is installed and running.

### **1️⃣ Build the Docker Image**  

```bash
cd fastapi_uuid_server
```
```bash
docker build --no-cache -t fastapi-uuid .

```

### **2️⃣ Run the Container**  

```bash
docker run -d -p 9090:9090 --name fastapi-uuid fastapi-uuid
```

This exposes the API at **[http://127.0.0.1:9090](http://127.0.0.1:9090)**  

### **3️⃣ Running Tests in Docker**  

```bash
docker exec -it fastapi-uuid /bin/bash
poetry run pytest
```
---


🚀 **If you have any questions, feel free to reach out.**

