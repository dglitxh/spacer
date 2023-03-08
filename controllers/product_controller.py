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
                detail="Failed to create Product.",
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
                detail="Failed to create Product.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        product = await models.Product.get_or_none(id=id)
        return product
    except Exception as e:
        logger.error(e)
        raise http_exception

@router.get("/update", summary="Update product.")
async def upd_product(data: schema.Product) -> schema.Product:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create Product.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        product = await model.Product.get_or_none(id=data.id)
        product.update_from_dict(data.dict(exclude_unset=True))
        logger.info("Product succesfully updated.")
        return product
    except Exception as e:
        logger.error(e)
        raise http_exception


@router.delete("/{id}/remove", summary="Delete product")
async def delete_product(data: schema.Product) -> schema.Product:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to delete product.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        product = await models.Product.get_or_none(id=id)
        product.update_from_dict(data.dict(exclude_unset=True))
        await product.delete()
        logger.info("Product deleted succesfully")
        return product
    except Exception as e:
        logger.error(e)
        raise http_exception