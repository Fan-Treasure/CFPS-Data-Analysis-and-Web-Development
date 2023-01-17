from pydantic import BaseModel


class register(BaseModel):
    username: str
    password: str


class login(BaseModel):
    username: str
    password: str


class change_password(BaseModel):
    username: str
    new_password: str