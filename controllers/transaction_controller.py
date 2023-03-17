import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv


router = APIRouter(prefix="/transactions")

@router.post("/withdraw")
async def withdraw_from_store(amount: float):
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