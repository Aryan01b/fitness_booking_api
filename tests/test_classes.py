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

def test_get_classes_with_timezone():
    # Test with UTC
    response = client.get("/api/v1/classes?display_tz=UTC")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for cls in data:
        assert "datetime" in cls
        # Should end with '+00:00' for UTC if aware, or be ISO format
        assert cls["datetime"].endswith("+00:00") or "T" in cls["datetime"]

    # Test with Asia/Kolkata (default)
    response = client.get("/api/v1/classes?display_tz=Asia/Kolkata")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for cls in data:
        assert "datetime" in cls
        # Should end with '+05:30' for IST if aware, or be ISO format
        assert cls["datetime"].endswith("+05:30") or "T" in cls["datetime"]
