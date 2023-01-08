import os
import logging
from tortoise import Tortoise, run_async
from dotenv import load_dotenv
import models.models as models
import time

load_dotenv()
db = os.getenv("DB_URL")

async def init_db():
    try:
        print("initializing database")
        await Tortoise.init(
            db_url=db,
            modules = {
                "models": [models]
            }
        )
        await Tortoise.generate_schemas()
        logging.info("database initialized succesfully.")
        print("initialized db")
    except Exception as e:
        logging.error("there was an error initializing db")
        print(e)

run_async(init_db())