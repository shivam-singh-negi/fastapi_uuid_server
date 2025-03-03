import uuid
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_uuid_success():
    """Test successful UUID generation from /uuid endpoint."""
    # Arrange & Act
    response = client.get("/uuid")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "uuid" in data
    assert "execution_time_seconds" in data
    assert isinstance(data["uuid"], str)
    
    # Validate the UUID format
    try:
        uuid_obj = uuid.UUID(data["uuid"], version=4)
        assert str(uuid_obj) == data["uuid"]
    except ValueError:
        assert False, "Invalid UUID returned"

def test_generate_async_uuid_success():
    """Test successful UUID generation with delay from /async-uuid endpoint."""
    # Arrange & Act
    response = client.get("/async-uuid")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "uuid" in data
    assert "execution_time_seconds" in data
    assert isinstance(data["uuid"], str)
    
    # Validate the UUID format
    try:
        uuid_obj = uuid.UUID(data["uuid"], version=4)
        assert str(uuid_obj) == data["uuid"]
    except ValueError:
        assert False, "Invalid UUID returned"
    
    # Ensure the delay was at least 3 seconds
    assert data["execution_time_seconds"] >= 3, (
        f"Execution time was {data['execution_time_seconds']}, expected at least 3 seconds"
    )

def test_generate_uuid_internal_error():
    """Test internal error handling for /uuid endpoint."""
    with patch("app.main.uuid.uuid4", side_effect=Exception("Test error")):
        response = client.get("/uuid")
        
        assert response.status_code == 500
        data = response.json()
        assert "detail" in data
        assert "Error generating UUID" in data["detail"]

def test_generate_async_uuid_internal_error():
    """Test internal error handling for /async-uuid endpoint."""
    with patch("app.main.uuid.uuid4", side_effect=Exception("Test error")):
        response = client.get("/async-uuid")
        
        assert response.status_code == 500
        data = response.json()
        assert "detail" in data
        assert "Error generating async UUID" in data["detail"]
