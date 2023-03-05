import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv

router = APIRouter(prefix="/products")

@router.post("/new", summary="Create a product.")
async def add_product(data: schema.Product) -> schema.Product:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create store.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        product = await models.Product.create(**data.dict())
        logger.info("product created succesfully")
        return product
    except Exception as e:
        logger.error(e)
        raise http_exception


@router.get("/{id}", summary="Create a product.")
async def get_product(data: schema.Product) -> schema.Product:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create store.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        product = await models.Product.get_or_none(id=id)
        return product
    except Exception as e:
        logger.error(e)
        raise http_exception