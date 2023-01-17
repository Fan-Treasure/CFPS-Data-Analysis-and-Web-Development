from pydantic import BaseModel


class Auth(BaseModel):
    token: str