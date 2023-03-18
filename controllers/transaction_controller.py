import os
import json
from ..common.logger import logger
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv


router = APIRouter(prefix="/transactions")

@router.post("stores/{id}/withdraw")
async def withdraw_from_store(amount: float, id: int):
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to withdraw money.",
                headers={"WWW-Authenticate": "Bearer"},)
    try:
        store = await models.Store.get_or_none(id=id)
        if store:
            if amount > store.cash_total:
                raise http_exception
            # withraw money
    except Exception as e:
        logger.error(e)
        return

@router.get("orders/{id}/payment")
async def pay_order(id: int):
     http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to withdraw money.",
                headers={"WWW-Authenticate": "Bearer"},)

    try:
        order = await models.Order.get_or_none(id=id)
        if not order:
            raise http_exception
        amt = order.