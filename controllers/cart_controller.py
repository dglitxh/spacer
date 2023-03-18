import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv
from ..main import cart

router = APIRouter(prefix="/cart")

@router.post("/add")
async def add_item(item) -> schema.CartItem:
    try:
        return cart.add_to_cart(item)
    except Exception as e:
        logger.error(e)
        return 

@router.delete("/{id}/remove")
async def remove_item(item):
    try: 
        return cart.remove_from_cart(item)
    except Exception as e:
        logger.error(e)
        return

@router.get("/items")
async def get_items():
    try: 
        cart.get_cart()
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