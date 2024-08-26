from fastapi.testclient import TestClient
import pytest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.auth import verify_token
from app.database import Base, get_db


@pytest.fixture
def setup():
    SQLALCHEMY_DATABASE_URL = "sqlite://"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


def override_dependency():
    pass


app.dependency_overrides[verify_token] = override_dependency


def test_get_employees(setup):
    response = client.get("/employees/")
    assert response.status_code == 200
    assert response.json() == []


def test_post_employee(setup):
    response = client.post(
        "/employees/",
        json={
            "first_name": "test",
            "last_name": "testing",
            "email": "test@test.com",
            "employee_type": "regular",
            "properties": {},
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "test",
        "last_name": "testing",
        "email": "test@test.com",
        "employee_type": "regular",
        "properties": {},
        "id": 1,
    }


def test_get_employee(setup):
    client.post(
        "/employees/",
        json={
            "first_name": "test",
            "last_name": "testing",
            "email": "test@test.com",
            "employee_type": "regular",
            "properties": {},
        },
    )
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "test",
        "last_name": "testing",
        "email": "test@test.com",
        "employee_type": "regular",
        "properties": {},
        "id": 1,
    }


def test_put_employee(setup):
    client.post(
        "/employees/",
        json={
            "first_name": "test",
            "last_name": "testing",
            "email": "test@test.com",
            "employee_type": "regular",
            "properties": {},
        },
    )
    response = client.put(
        "/employees/1",
        json={
            "first_name": "testedited",
            "last_name": "testingedited",
            "email": "testedited@test.com",
            "employee_type": "contractual",
            "properties": {"test": "test"},
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "testedited",
        "last_name": "testingedited",
        "email": "testedited@test.com",
        "employee_type": "contractual",
        "properties": {"test": "test"},
        "id": 1,
    }


def test_delete_employee(setup):
    client.post(
        "/employees/",
        json={
            "first_name": "test",
            "last_name": "testing",
            "email": "test@test.com",
            "employee_type": "regular",
            "properties": {},
        },
    )
    response = client.delete("/employees/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted successfully"}
    response = client.get("/employees/")
    assert response.status_code == 200
    assert response.json() == []
