import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv
from commom.logger import logger

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
        cart = await rdb.get("cart_key")
        if cart:
            for item in cart:
                await models.OrderItem.create(**item.dict())
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
        order.update_from_dict(dict(data, exclude_unset=True))
        await order.save()
        logger.info("order succesfully updated.")
        return order
    except Exception as e:
        logger.error(e)
        raise http_exception


@router.get("/{id}/get", summary="Update order.")
async def upd_order(id: int) -> schema.Order:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create order.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        order = await models.Order.get_or_none(id=id)
        return order
    except Exception as e:
        logger.error(e)
        raise http_exception


@router.get("/stores/{id}/get_orders")
async def get_store_orders(id: int) -> schema.Order:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create order.",
                headers={"WWW-Authenticate": "Bearer"},
            )

    try:
        orders = await models.Store.filter(store_id=id)
        return orders
    except Exception as e:
        logger.error(e)
        raise http_exception


@router.delete("/{id}/delete", summary="delete order")
async def delete_order(id: int) -> schema.Order:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to delete order.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        order = await models.Order.get_or_none(id=id)
        if order:
            await order.delete()
        return order
    except Exception as e:
        logger.error(e)
        raise http_exception