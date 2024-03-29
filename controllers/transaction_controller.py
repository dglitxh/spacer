import os
import json
import requests
from common.logger import logger
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv
from .cart import cart


router = APIRouter(prefix="/transactions")

@router.post("/stores/{id}/withdraw")
async def withdraw_from_store(amount: float, id: int):
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to withdraw money.",
                headers={"WWW-Authenticate": "Bearer"},)
    try:
        store = await models.Store.get_or_none(id=id)
        amount *= 0.98
        if store:
            if amount > store.cash_total:
                raise http_exception
            # withraw money
            store.cash_total -= amount
            store.update_from_dict(dict(store), exclude_unset=True)
            store.save()
        logger.info("Cash withdrawal was succesful")
    except Exception as e:
        logger.error(e)
        return

@router.get("/orders/{id}/payment")
async def pay_order(id: int):
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to complete payment.",
                headers={"WWW-Authenticate": "Bearer"},)

    try:
        order = await models.Order.get_or_none(id=id)
        store = await models.Store.get_or_none(id=order.store_id)
        if not order:
            raise http_exception
        amt = cart.get_total()
        # make your payment. 
        verify = await requests.get("")
        if verify:
            store = await models.Store.get_or_none(id=order.store_id)
            store.cash_total += amt
            store.update_from_dict(dict(store), exclude_unset=True)
            await store.save()
            order.paid = True
            order.update_from_dict(dict(order), exclude_unset=True)
            await order.save()
            logger.info("Payment was succesfull.")
    except Exception as e:
        logger.error(e)
        raise http_exception