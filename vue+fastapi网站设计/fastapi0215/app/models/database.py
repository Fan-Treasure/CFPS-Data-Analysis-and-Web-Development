from pydantic import BaseModel


class get_table(BaseModel):
    table_name: str


class curd(BaseModel):
    sql_code: str


class get_cols(BaseModel):
    tip: dict


class select_cols(BaseModel):
    tip: dict


class page1(BaseModel):
    table_name: str
    page: int


class page2(BaseModel):
    sql_code: str
    page: int


class page3(BaseModel):
    tip: dict
    page: int