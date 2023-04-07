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
        add = await cart.add_to_cart(dict(product), item.quantity)
        return add
    except Exception as e:
        logger.error(e)
        return 

@router.delete("/{id}/remove")
async def remove_item(item):
    try: 
        rem = await cart.remove_from_cart(item)
        return rem
    except Exception as e:
        logger.error(e)
        return

@router.get("/items")
async def get_items():
    try: 
        cart = cart.get_cart()
        return cart
    except Exception as e:
        logger.error(e)
        return 

@router.get("/total")
async def get_cart_total():
    try: 
        return cart.get_total()
    except Exception as e:
        logger.error(e)
        return