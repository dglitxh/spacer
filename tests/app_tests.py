import httpx
from main import app
from fastapi.testclient import TestClient
from common.logger import logger
from common.db import rdb

client = TestClient(app)

prod = {
    "name": "Big Clothing", 
    "description": "This is just a piece of clothing",
    "category": "clothing",
    "rating": 0.0,
    "price": 30,
    "store_id": 1
}

store = {
    "name": "Big store", 
    "description": "we sell big tings",
    "category": "groceries",
    "cash_total": 20.2,
    "owner_id": 1
}

def test_create_prod():
    response =  client.post("/products/new", json=prod)
    json = response.json()
    logger.info(json)
    assert response.status_code == 200
    assert json == prod

def test_get_prod():
    response = client.get("/products/2/get")
    json = response.json()
    logger.info(json)
    assert response.status_code == 200

def test_get_prod():
    response = client.get("/products/2/delete")
    json = response.json()
    logger.info(json)
    assert response.status_code == 200