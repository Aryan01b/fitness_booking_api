from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_booking():
    # First, get a class_id
    classes_response = client.get("/classes/")
    assert classes_response.status_code == 200
    classes = classes_response.json()
    assert len(classes) > 0
    class_id = classes[0]["id"]

    # Book a slot
    booking_payload = {
        "class_id": class_id,
        "client_name": "John Doe",
        "client_email": "john@example.com"
    }
    response = client.post("/bookings/book", json=booking_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["class_id"] == class_id
    assert data["client_name"] == "John Doe"
    assert data["client_email"] == "john@example.com"

def test_get_bookings_by_email():
    # Should return bookings for John
    response = client.get("/bookings/", params={"email": "john@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["client_email"] == "john@example.com"
