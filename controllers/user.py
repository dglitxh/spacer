from ..models import models, schema
import logging

async def signup(creds: models.User) -> schema.User:
    user = await models.User.create(creds)
    return user

    
