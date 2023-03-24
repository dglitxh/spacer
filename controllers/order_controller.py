import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv

router = APIRouter(prefix="/order")

@router.post("/new", summary="Create a order.")
async def add_order(data: schema.Order) -> schema.Order:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create order.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        order = await models.Order.create(**data.dict())
        logger.info("order created succesfully")
        return order
    except Exception as e:
        logger.error(e)
        raise http_exception