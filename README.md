# Fitness Studio Booking API

A high-performance RESTful API for managing fitness class bookings at OmniFit Studios. Built with FastAPI, this API provides a robust solution for class management, booking, and user management.

## 🚀 Features

- Browse upcoming fitness classes with real-time availability
- Comprehensive class and booking management
- Timezone-aware scheduling (IST by default)
- Input validation and error handling
- Automated testing with pytest
- API documentation with Swagger UI

## 🛠️ Tech Stack

- **Framework**: FastAPI (Python 3.9+)
- **Database**: SQLAlchemy
- **Testing**: pytest
- **Linting**: flake8, black
- **Documentation**: Swagger UI, Redoc

## 🚀 Getting Started

### Prerequisites

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
- ReDoc: `http://localhost:8000/redoc`

### Available Endpoints

#### Classes
- `GET /api/v1/classes` - List all upcoming fitness classes

#### Bookings
- `POST /api/v1/book` - Create a new booking
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