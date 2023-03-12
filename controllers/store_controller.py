import os
import json
from models import models, schema
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from dotenv import load_dotenv

router = APIRouter(prefix="/store")

@router.post("/new", summary="Create a store.")
async def add_store(data: schema.Store) -> schema.Store:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create store.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        data.cash_total = 0.0
        store = await models.Store.create(**data.dict())
        logger.info("store created succesfully")
        return store
    except Exception as e:
        logger.error(e)
        raise http_exception

@router.get("/{id}", summary="Get store from db.")
async def get_store(id: int) -> schema.Store:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to fetch store.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        store = await models.Store.get_or_none(id=id)
        return store
    except Exception as e:
        logger.error(e)
        raise http_exception

@router.put("/{id}/update", summary="update store")
async def upd_store(data: schema.Store, id: int) -> schema.Store:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create store.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        store = await models.Store.get_or_none(id=id)
        store.update_from_dict(data.dict(exclude_unset=True))
        await store.save()
        logger.info("store updated succesfully")
        return store
    except Exception as e:
        logger.error(e)
        raise http_exception

@router.delete("/{id}/remove", summary="Delete store")
async def delete_store(data: schema.Store, id: int) -> schema.Store:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to delete store.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        store = await models.Store.get_or_none(id=id)
        store.update_from_dict(data.dict(exclude_unset=True))
        await store.delete()
        logger.info("store deleted succesfully")
        return store
    except Exception as e:
        logger.error(e)
        raise http_exception

@router.get("/{st_id}/products", summary="Create a product.")
async def get_store_products(data: schema.Product) -> schema.Product:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create store.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        product = await models.Product.filter(store_id=query.st_id)
        logger.info("product created succesfully")
        return product
    except Exception as e:
        logger.error(e)
        raise http_exception

@router.put("/{id}/update_income", summary="update store")
async def upd_store(amt: float, id: int) -> schema.Store:
    http_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to create store.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    try:
        store = await models.Store.get_or_none(id=id)
        store.cash_total = amt
        store.update_from_dict(data.dict(exclude_unset=True))
        await store.save()
        logger.info("store updated succesfully")
        return store
    except Exception as e:
        logger.error(e)
        raise http_exception