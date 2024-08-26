from fastapi.testclient import TestClient

from app.main import app
from app.auth import verify_token

client = TestClient(app)


def override_dependency():
    pass


app.dependency_overrides[verify_token] = override_dependency


def test_get_auth():
    response = client.get("/auth")
    assert response.status_code == 200
    assert response.json() == {"message": "success"}
