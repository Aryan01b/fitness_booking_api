from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_booking():
    # First, get a class_id
    classes_response = client.get("/api/v1/classes")
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
    response = client.post("/api/v1/book", json=booking_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["class_id"] == class_id
    assert data["client_name"] == "John Doe"
    assert data["client_email"] == "john@example.com"


def test_duplicate_booking_same_email_fails():
    # First, get a class_id
    classes_response = client.get("/api/v1/classes")
    assert classes_response.status_code == 200
    classes = classes_response.json()
    assert len(classes) > 0
    class_id = classes[0]["id"]

    booking_payload = {
        "class_id": class_id,
        "client_name": "Jane Doe",
        "client_email": "janedup@example.com"
    }
    # First booking should succeed
    response1 = client.post("/api/v1/book", json=booking_payload)
    assert response1.status_code == 200
    # Second booking with same email and class should fail
    response2 = client.post("/api/v1/book", json=booking_payload)
    assert response2.status_code == 400
    assert "already booked" in response2.json()["detail"].lower()


def test_booking_fails_when_no_slots():
    # Find a class with zero slots
    classes_response = client.get("/api/v1/classes")
    assert classes_response.status_code == 200
    classes = classes_response.json()
    zero_slot_class = next((c for c in classes if c["available_slots"] == 0), None)
    assert zero_slot_class is not None, "No class with zero slots found."
    booking_payload = {
        "class_id": zero_slot_class["id"],
        "client_name": "Zero Slot",
        "client_email": "zeroslot@example.com"
    }
    response = client.post("/api/v1/book", json=booking_payload)
    assert response.status_code == 400
    assert "no slots available" in response.json()["detail"].lower()

def test_get_bookings_by_email():
    # Should return bookings for John
    response = client.get("/api/v1/bookings", params={"email": "john@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["client_email"] == "john@example.com"
