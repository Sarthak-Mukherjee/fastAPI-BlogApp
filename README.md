# FastAPI Blog Application

A modern, production-ready REST API built with FastAPI and PostgreSQL for managing blog posts and user accounts.

## Overview

This project demonstrates a full-featured backend API with user authentication, post management, and database persistence. It showcases best practices in API design, database management, and Python development.

## Features

- **User Management**
  - Create new user accounts
  - Retrieve user information by ID
  - Secure password hashing with bcrypt

- **Post Management**
  - Create, read, and manage blog posts
  - Track post metadata (creation timestamp, publication status)
  - List all published and unpublished posts

- **Database**
  - PostgreSQL integration with SQLAlchemy ORM
  - Automatic database schema generation
  - Timestamp tracking for data auditing

- **API Documentation**
  - Auto-generated Swagger UI at `/docs`
  - ReDoc documentation at `/redoc`

## Tech Stack

- **Framework**: FastAPI 0.116.1
- **Database**: PostgreSQL with SQLAlchemy 2.0.43
- **Server**: Uvicorn
- **Validation**: Pydantic 2.11.7
- **Security**: bcrypt with Passlib

## Project Structure

```
fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── models.py               # SQLAlchemy database models
│   ├── schemas.py              # Pydantic validation schemas
│   ├── database.py             # Database configuration
│   ├── utils.py                # Utility functions
│   └── routers/
│       ├── post.py             # POST endpoints
│       └── user.py             # USER endpoints
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```


4. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## API Endpoints

### Users
- `POST /users/` - Create a new user
- `GET /users/{id}` - Get user by ID

### Posts
- `GET /posts/` - Retrieve all posts
- `POST /posts/` - Create a new post
- `GET /posts/{id}` - Get post by ID

## Database Schema

### Users Table
- `id` (Integer, Primary Key)
- `email` (String, Unique)
- `password` (String, Hashed)
- `created_at` (Timestamp)

### Posts Table
- `id` (Integer, Primary Key)
- `title` (String)
- `content` (String)
- `published` (Boolean, Default: True)
- `created_at` (Timestamp)

## Usage Examples

### Create a User
```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d "{\"email\": \"user@example.com\", \"password\": \"securepassword\"}"
```

### Create a Post
```bash
curl -X POST "http://localhost:8000/posts/" \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"My First Post\", \"content\": \"This is my first blog post\", \"published\": true}"
```

### Get All Posts
```bash
curl "http://localhost:8000/posts/"
```

## Development

### View API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Run in Development Mode
```bash
uvicorn app.main:app --reload
```

The `--reload` flag enables auto-restart when code changes are detected.

## Security Considerations

- Passwords are hashed using bcrypt before storage
- Email validation is enforced
- Consider implementing JWT authentication for protected endpoints
- Never commit credentials to version control

## Future Enhancements

- JWT token-based authentication
- Post update and delete endpoints
- User update and delete endpoints
- Post ownership and permissions
- Search and filtering capabilities
- Rate limiting
- CORS configuration

## Troubleshooting

### Database Connection Failed
- Ensure PostgreSQL is running
- Verify connection credentials in [main.py](app/main.py)
- Check that the `fastapi` database exists

### Module Import Errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again
- Check that all files are in the correct directory structure

## License

This project is provided as-is for educational purposes.
