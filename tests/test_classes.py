from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/api/v1/classes")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "name" in data[0]
    assert "datetime" in data[0]
    assert "instructor" in data[0]
    assert "available_slots" in data[0]
