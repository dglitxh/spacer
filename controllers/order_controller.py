import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv
from common.logger import logger

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
                o_item = {}
                o_item["order_id"] = data.id
                o_item["product_id"] = item.product
                o_item["quantity"] = item.quantity
                o_item["total_price"] = item.quantity * item.price
                await models.OrderItem.create(**item.o_item())
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

@router.get("/{id}/get_items", summary="delete order")
async def get_order_items(id: int) -> schema.Order:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to get order items.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        order_items = await models.OrderItem.filter(order_id=id)
        return order_items
    except Exception as e:
        logger.error(e)
        raise http_exception

@router.get("/all", summary="get all orders")
async def get_orders():
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to get order items.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        orders = await models.Order.all().limit(50)
        return orders
    except Exception as e:
        logger.error(e)
        raise http_exception