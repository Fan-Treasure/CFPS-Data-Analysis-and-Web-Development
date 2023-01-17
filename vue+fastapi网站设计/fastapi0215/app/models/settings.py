import datetime

from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = "e843b11f07f51af3653218f49af08d35e44432b5d17b8737d5093f8b1c5b80aa"
    authjwt_access_token_expires: datetime.timedelta = datetime.timedelta(minutes=480)
