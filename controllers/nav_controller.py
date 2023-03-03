import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv

router = APIRouter(prefix="/store")

@router.post("/new", summary="Create an account")
async def add_store(data: schema.Store) -> schema.Store:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create store.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        store = await models.User.create(**data.dict())
        logger.info("store created succesfully")
        return client
    except Exception as e:
        logger.error(e)
        raise http_exception