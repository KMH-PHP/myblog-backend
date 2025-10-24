# MyBlog API

A FastAPI-based blog application with user authentication and CRUD operations for blog posts.

## Features

- User authentication with JWT tokens
- CRUD operations for blog posts
- PostgreSQL database integration
- RESTful API endpoints
- CORS support for frontend integration

## Prerequisites

- Python 3.8+
- PostgreSQL database
- Git

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/KMH-PHP/myblog-backend.git
cd myblog
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### Option A: Using PostgreSQL (Recommended)

1. Install PostgreSQL on your system
2. Create a database:
   ```sql
   CREATE DATABASE blog;
   ```
3. Create a user (optional):
   ```sql
   CREATE USER postgres WITH PASSWORD 'helloworld';
   GRANT ALL PRIVILEGES ON DATABASE blog TO postgres;
   ```

#### Option B: Using Docker for PostgreSQL

```bash
# Run PostgreSQL container
docker run --name postgres-blog -e POSTGRES_PASSWORD=helloworld -e POSTGRES_DB=blog -p 5432:5432 -d postgres:latest
```

### 5. Configure Database Connection

Edit the `app/database.py` file to match your PostgreSQL configuration:

```python
DATABASE_URL = "postgresql://username:password@localhost/database_name"
```

Default configuration (as in the code):
```python
DATABASE_URL = "postgresql://postgres:helloworld@localhost/blog"
```

## Running the Application

### Method 1: Direct Run

```bash
# Navigate to project root
cd myblog

# Run the FastAPI application
uvicorn app.main:app --reload
```

### Method 2: Using Python Module

```bash
# From project root
python -m uvicorn app.main:app --reload
```

### Method 3: Using a Run Script (Optional)

Create a `run.sh` file:

```bash
#!/bin/bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Make it executable and run:
```bash
chmod +x run.sh
./run.sh
```

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## API Endpoints

### Authentication

- `POST /auth/` - Create a new user
- `POST /auth/token` - Login and get access token

### Blog Operations

- `GET /` - Get current user info (requires authentication)
- `GET /blogs/{user_id}` - Get all blogs for a specific user
- `POST /blogs/user/{user_id}` - Create a new blog post
- `GET /blogs/title/{title}` - Get blog by title
- `PUT /blogs/{blog_id}` - Update a blog post
- `DELETE /blogs/{blog_id}` - Delete a blog post
- `GET /users` - Get all users

## Usage Examples

### 1. Create a User

```bash
curl -X POST "http://localhost:8000/auth/" \
-H "Content-Type: application/json" \
-d '{"username": "john_doe", "password": "securepassword"}'
```

### 2. Login and Get Token

```bash
curl -X POST "http://localhost:8000/auth/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=john_doe&password=securepassword"
```

### 3. Create a Blog Post (with authentication)

```bash
curl -X POST "http://localhost:8000/blogs/user/1" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{"title": "My First Blog", "sub_title": "An introduction", "content": "This is my blog content..."}'
```

## Development

### Project Structure

```
myblog/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and routes
│   ├── models.py        # SQLAlchemy database models
│   ├── schema.py        # Pydantic models/schemas
│   ├── crud.py          # CRUD operations
│   ├── auth.py          # Authentication logic
│   └── database.py      # Database configuration
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

### Adding New Features

1. Add new models in `app/models.py`
2. Create corresponding schemas in `app/schema.py`
3. Implement CRUD operations in `app/crud.py`
4. Add API endpoints in `app/main.py`

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure PostgreSQL is running
   - Check database credentials in `app/database.py`
   - Verify the database exists

2. **Module Import Errors**
   - Make sure you're in the project root directory
   - Activate the virtual environment
   - Install all dependencies: `pip install -r requirements.txt`

3. **Port Already in Use**
   - Change the port: `uvicorn app.main:app --port 8001`
   - Or kill the process using the port

### Environment Variables (Optional)

You can create a `.env` file for configuration:

```env
DATABASE_URL=postgresql://postgres:helloworld@localhost/blog
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
```

Then modify `app/database.py` and `app/auth.py` to use these variables.

## Production Deployment

For production deployment, consider:

1. Using a production-grade ASGI server like Gunicorn with Uvicorn workers
2. Setting up proper environment variables
3. Configuring a reverse proxy (Nginx)
4. Setting up SSL/TLS certificates
5. Database connection pooling
6. Logging and monitoring

Example production command:
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
