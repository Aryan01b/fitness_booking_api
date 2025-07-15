# 🧘‍♂️ Fitness Studio Booking API

A simple, modern API for fitness studios to manage class schedules and allow users to book workout sessions online.

- Studio owners can list classes, set available slots, and track bookings.
- Users can view all available fitness classes and reserve a spot instantly—no double booking or overbooking allowed!

Ideal for gyms, yoga studios, and group fitness instructors looking for a fast, reliable way to handle class signups and attendance.

---

## 🚀 Features

- View all available fitness classes
- Book a class (prevents duplicate bookings per email/class and overbooking)
- List bookings by email
- SQLite in-memory database (easy to swap for persistent storage)
- Robust API validation & error handling
- Fully tested with pytest

---

## 🛠 Tech Stack

- **Framework:** FastAPI
- **ORM/Database:** SQLAlchemy with SQLite (in-memory for dev)
- **Validation:** Pydantic
- **Testing:** Pytest
- **Dependency Management:** pip
- **API Docs:** Swagger UI (OpenAPI)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aryan01b/fitness_booking_api.git
   cd fitness_booking_api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


### Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`

---

## ⏰ Time Zone Support

The API supports only IANA time zone names (also known as tz database names, e.g. `Asia/Kolkata`, `America/New_York`).

- **Abbreviations** like `IST`, `PST`, `CET`, etc., are not supported and will result in a 400 Bad Request error.
- Use the full IANA name as accepted by the [pytz](http://pytz.sourceforge.net/) library.

Below are some common IANA time zones for reference:

| IANA Time Zone Name    | Typical UTC Offset                | Example Abbreviation | Major City Example   |
|-----------------------|-----------------------------------|---------------------|---------------------|
| America/New_York      | UTC−05:00 (EST) / UTC−04:00 (EDT) | EST / EDT           | New York            |
| America/Los_Angeles   | UTC−08:00 (PST) / UTC−07:00 (PDT) | PST / PDT           | Los Angeles         |
| Europe/Berlin         | UTC+01:00 (CET) / UTC+02:00 (CEST)| CET / CEST          | Berlin              |
| Europe/London         | UTC±00:00 (GMT) / UTC+01:00 (BST) | GMT / BST           | London              |
| Asia/Kolkata          | UTC+05:30                         | IST                 | Delhi, Mumbai       |

For a full list, see the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

---

### Available Endpoints

#### Classes
- `GET /api/v1/classes` — List all upcoming fitness classes

#### Bookings
- `POST /api/v1/book` — Create a new booking
- `GET /api/v1/bookings` — List bookings by email

## 🧪 Running Tests

Run the test suite with:
```bash
pytest --cov=app --cov-report=term-missing
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
