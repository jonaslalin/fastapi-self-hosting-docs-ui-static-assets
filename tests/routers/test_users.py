from fastapi.testclient import TestClient

from myapi.app.main import app

client = TestClient(app)


def test_read_user() -> None:
    response = client.get("/users/guido")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Guido!"}
