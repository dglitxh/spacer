import os
from .logger import logger
from tortoise import Tortoise
from dotenv import load_dotenv
from redis import asyncio as redis
from tortoise.contrib.fastapi import register_tortoise

load_dotenv()
db = os.getenv("DB_URL") 
rds_url = os.getenv("RDS_URL")

TORTOISE_ORM = {
    "connections": {"default": db},
    "apps": {
        "models": {
            "models": ["models.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

def init_db(app):
    try:
        register_tortoise(
            app,
            config=TORTOISE_ORM,
            generate_schemas=True,
            add_exception_handlers=True,
        )
        logger.info("database initialized succesfully.")
    except Exception as e:
        logger.error("there was an error initializing db")


def init_rdb():
    try:
        r = redis.Redis(host=rds_url,port=6379, decode_responses=True )
        return r
    except Exception as e:
        logger.error("Redis failed to start...")

rdb = init_rdb()
