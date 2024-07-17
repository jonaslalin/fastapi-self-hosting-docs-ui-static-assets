from fastapi import APIRouter
from typing_extensions import TypedDict


class HelloMessage(TypedDict):
    message: str


router = APIRouter()


@router.get("/users/{username}")
async def read_user(username: str) -> HelloMessage:
    return {"message": f"Hello, {username.capitalize()}!"}
