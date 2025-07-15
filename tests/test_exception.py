from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_http_exception_handled():
    # Try to book a class with an invalid class_id (should raise 404 HTTPException)
    payload = {
        "class_id": 99999,  # unlikely to exist
        "client_name": "Test Exception",
        "client_email": "testexc@example.com"
    }
    resp = client.post("/api/v1/book", json=payload)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Class not found"

def test_unhandled_exception_handled(monkeypatch):
    # Patch a route to raise an unhandled exception
    @app.get("/raise-unhandled-error")
    def raise_error():
        raise ValueError("This is a test error!")

    resp = client.get("/raise-unhandled-error")
    assert resp.status_code == 500
    assert resp.json()["detail"] == "Internal Server Error"
