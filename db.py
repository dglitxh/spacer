import os
import logging
from tortoise import Tortoise, run_async
from dotenv import load_dotenv
import models.models as models

load_dotenv()
db = os.getenv("DB_URL")

async def init_db():
    print("ddododododod")
    await Tortoise.init(
        db_url=db,
        modules = {
            "models": ["models.models"]
        }
    )
    await Tortoise.generate_schemas()
    logging.info("database initialized")
    print("init db")

      