import pytest
from fastapi.testclient import TestClient

from myapi.app.main import app


@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(app)


def test_read_user(client: TestClient) -> None:
    response = client.get("/users/guido")
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, guido!"}
