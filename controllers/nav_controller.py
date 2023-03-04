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
        store = await models.Store.create(**data.dict())
        logger.info("store created succesfully")
        return store
    except Exception as e:
        logger.error(e)
        raise http_exception

@router.post("/{id}/get", summary="Create an account")
async def get_store(data: schema.Store) -> schema.Store:
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

@router.post("/{id}/update", summary="update store")
async def upd_store(data: schema.Store) -> schema.Store:
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

@router.post("/{id}/remove", summary="Delete store")
async def delete_store(data: schema.Store) -> schema.Store:
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
