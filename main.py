from typing import Union
from fastapi import FastAPI
import datetime
import json
from models.schema import Ticket
from models import models
from tortoise.contrib.pydantic import pydantic_model_creator
from common.db import init_db, rdb
from common.logger import logger
from controllers.user_controller import router as auth_router

app = FastAPI()
app.include_router(auth_router)
init_db(app)

@app.get("/")
async def home():
    return {"msg: get me lit"}

@app.on_event("startup")
async def ping():
    """
        pings redit by setting and getting a value.
    """
    await rdb.set("key", json.dumps({
        "PING":"PONG",
    }))
    key = await rdb.get("key")
    key = json.loads(key)
    print(key["PING"])

logger.info("We are live.")