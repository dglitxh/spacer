import os
from .logger import logger
from tortoise import Tortoise, run_async
from dotenv import load_dotenv
# from ..models import models
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
import time

load_dotenv()
db = os.getenv("DB_URL") 

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
        print(e)

