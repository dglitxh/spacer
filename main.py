from typing import Union
from fastapi import FastAPI
import datetime
from models.schema import Ticket
import models.models as models
from tortoise.contrib.pydantic import pydantic_model_creator
from common.db import init_db

app = FastAPI()
init_db(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/post")
async def read_item(ticket: Ticket):
    print(ticket)
    tick = await models.Ticket.create(**ticket.dict())
    print(post)
    return tick


