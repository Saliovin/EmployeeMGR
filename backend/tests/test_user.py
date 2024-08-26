import bcrypt
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.models.user import User


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

    db_session = TestingSessionLocal()
    admin_username = "admin"
    admin_password = "password"
    hashed_password = bcrypt.hashpw(admin_password.encode(), bcrypt.gensalt())
    admin = User(username=admin_username, hashed_password=hashed_password)
    db_session.add(admin)
    db_session.commit()

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


def test_post_login(setup):
    response = client.post(
        "/users/login", json={"username": "admin", "password": "password"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}


def test_post_logout(setup):
    response = client.post(
        "/users/logout", json={"username": "admin", "password": "password"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Logout successful"}
