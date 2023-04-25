import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv
from common.logger import logger
from .cart import cart

router = APIRouter(prefix="/cart")

@router.post("/add")
async def add_item(item: schema.OrderItem) -> schema.OrderItem:
    try:
        product = await models.Product.get_or_none(id=item.product_id)
        add = await cart.add_to_cart(dict(product), item.quantity, repl=False)
        return add
    except Exception as e:
        logger.error(e)
        return e

@router.post("/remove")
async def remove_item(item: schema.OrderItem):
    try: 
        product = await models.Product.get_or_none(id=item.product_id)
        rem = await cart.remove_from_cart(dict(product))
        return rem
    except Exception as e:
        logger.error(e)
        return e

@router.get("/items")
async def get_items():
    try: 
        mycart = cart.get_cart()
        return mycart
    except Exception as e:
        logger.error(e)
        return e

@router.get("/total")
async def get_cart_total():
    try: 
        total =  cart.get_total()
        return round(total, 2)
    except Exception as e:
        logger.error(e)
        return e

@router.get("/empty")
async def cart_empty():
    try:
        empty = await cart.empty_cart()
        return empty
    except Exception as e:
        logger.error(e)
        return e