import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv

router = APIRouter(prefix="/orders")

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

@router.get("/update", summary="Update order.")
async def upd_order(data: schema.Order) -> schema.Order:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create order.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        order = await model.Order.get_or_none(id=data.id)
        order.update_from_dict(dict(data), exclude_unset=True)
        await order.save()
        logger.info("order succesfully updated.")
        return order
    except Exception as e:
        logger.error(e)
        raise http_exception