# Sprout Exam - Backend

## Environment Variables

```sh
JWT_SECRET=secret-for-signing-jwt
```

## Project Setup

### Install requirements

```sh
pip install -r requirements.txt
```

### Run migrations

```sh
alembic upgrade head
```

### Create admin user

```sh
python -m app.scripts.create_admin
```

### Run ASGI Server

```sh
fastapi dev app/main.py
```

### Run Unit Tests

```sh
pytest
```

## Project Setup With Docker

### Build Docker Image

```sh
docker build -t sprout-backend .
```

### Run Docker Image

```sh
docker run -p 8080:80 sprout-backend:latest
```