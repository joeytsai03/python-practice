from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/double_str")
def double_str():
    return cal_double_str('hello ')

def cal_double_str(str) -> str:
    return str * 2

def type_check():
    str_content : str = 'str'
    int_content : int  = 'int'
    content = str_content + int_content

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}