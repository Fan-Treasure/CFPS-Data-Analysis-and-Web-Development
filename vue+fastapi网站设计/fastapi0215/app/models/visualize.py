from pydantic import BaseModel


class count(BaseModel):
    tip: dict
    tubiao: str
    region: str