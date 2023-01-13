from ..models import models, schema
from passlib.context import CryptContext
import logging

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hasher(password: str) -> str:
    hashed = pwd_context.hash(password)
    return hashed


async def signup(creds: models.User) -> schema.User:
    try:
        hashed_pass = hasher(creds.password)
        creds.password = hashed_pass
        user = await models.User.create(creds)
        return user
    except Exception as e:
        # need to create universal logger.
        logging.error("There was an error creating user")
        print(e)




