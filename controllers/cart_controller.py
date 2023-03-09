import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv
from .cart import Cart


cart = Cart()
router = APIRouter(prefix="/cart")

@router.post("/add")
async def add_item(item) -> schema.CartItem:
    try:
        cart.add_to_cart(item)
    except Exception as e:
        logger.error(e)
        return 

@router.delete("/{id}/remove")
async def remove_item(item):
    try: 
        cart.remove_from_cart(item)
    except Exception as e:
        logger.error(e)
        return
