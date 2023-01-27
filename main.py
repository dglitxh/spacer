from typing import Union
from fastapi import FastAPI
import datetime
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
async def rds():
    await rdb.set("key", "val")
    key = await rdb.get("key")
    print(key)

logger.info("We are live.")