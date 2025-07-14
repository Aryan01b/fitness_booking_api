# 🧘‍♂️ Fitness Studio Booking API

A robust **FastAPI** backend for managing fitness class bookings, supporting various workout types including Yoga, Zumba, HIIT, and more.  
Built with **SQLAlchemy ORM** and **Pydantic** for type safety and data validation.  
Designed to demonstrate production-ready API development practices with clean architecture.

---

## 🚀 Features

### Core Functionality
- **Class Management**
  - View all upcoming classes with filtering options
  - Get class details including name, schedule, instructor, and available slots
  - Automatic slot availability tracking

### Booking System
- **Class Booking**
  - Reserve spots in fitness classes with real-time validation
  - Prevent double bookings and handle concurrent requests
  - Email notifications for booking confirmations

### User Experience
- **Booking Management**
  - View all bookings by email
  - Cancel bookings (with proper validation)
  - Booking history with timestamps

### Technical Features
- **Database**
  - SQLite with in-memory storage for development
  - Easy migration to persistent storage
  - Pre-populated with sample data

- **API**
  - RESTful endpoints with proper HTTP methods
  - Request/response validation using Pydantic models
  - Comprehensive error handling
  - API versioning support

- **Testing**
  - Unit tests with `pytest`
  - Test coverage reporting
  - Integration tests for API endpoints

---

## 🛠 Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite (in-memory), SQLAlchemy
- **Data Validation**: Pydantic
- **Testing**: Pytest
- **Dependency Management**: Pip
- **API Documentation**: Swagger UI

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

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
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

### Available Endpoints

#### Classes
- `GET /api/v1/classes` - List all upcoming fitness classes

#### Bookings
- `POST /api/v1/bookings/book` - Create a new booking
- `GET /api/v1/bookings` - List bookings by email

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

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.