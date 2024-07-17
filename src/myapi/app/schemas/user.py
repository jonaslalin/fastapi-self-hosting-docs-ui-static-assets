from pydantic import BaseModel


class User(BaseModel):
    greeting: str
