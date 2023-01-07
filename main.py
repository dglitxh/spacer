from typing import Union
from tortoise import Tortoise
from fastapi import FastAPI
from db import init_db
from tortoise import run_async

app = FastAPI()

run_async(init_db())

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
