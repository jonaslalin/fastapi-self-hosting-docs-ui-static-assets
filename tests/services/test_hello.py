import pytest

from myapi.app.services.hello import HelloService


@pytest.fixture
def hello_service() -> HelloService:
    return HelloService()


def test_greet(hello_service: HelloService) -> None:
    assert hello_service.greet("guido") == "Hello, guido!"
