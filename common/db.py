import os
import logging
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
        print("initializing database")
        register_tortoise(
            app,
            config=TORTOISE_ORM,
            generate_schemas=True,
            add_exception_handlers=True,
        )
        logging.info("database initialized succesfully.")
        print("initialized db")
    except Exception as e:
        logging.error("there was an error initializing db")
        print(e)

