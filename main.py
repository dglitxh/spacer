from typing import Union
from fastapi import FastAPI
import datetime
import json
from tortoise.contrib.pydantic import pydantic_model_creator
from common.db import init_db, rdb
from common.logger import logger
from controllers.user_controller import router as auth_router
from controllers.store_controller import router as store_router
from controllers.product_controller import router as product_router
from controllers.cart_controller import router as cart_router
from controllers.order_controller import router as order_controller

app = FastAPI()
app.include_router(auth_router)
app.include_router(store_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(order_controller)

@app.get("/")
async def home():
    return {"msg: get me lit"}

@app.on_event("startup")
def database_init():
    init_db(app)

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

logger.info("Spacer is running.")