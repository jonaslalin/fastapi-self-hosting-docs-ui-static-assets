from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from ..schemas.user import User
from ..services.hello import HelloService

router = APIRouter()


@router.get("/users/{username}")
async def read_user(username: str, hello_service: Annotated[HelloService, Depends()]) -> User:
    return User(greeting=hello_service.greet(username))
