import os
import logging
from tortoise import Tortoise, run_async
from dotenv import load_dotenv
import models.models as models
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
import time

load_dotenv()
db = os.getenv("DB_URL") 

def init_db(app):
    try:
        print("initializing database")
        register_tortoise(
            app,
            db_url=db,
            modules = {
                "models": [models]
            },
            generate_schemas=True,
            add_exception_handlers=True,
        )
        logging.info("database initialized succesfully.")
        print("initialized db")
    except Exception as e:
        logging.error("there was an error initializing db")
        print(e)

