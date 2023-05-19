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

def test_del_prod():
    response = client.delete("/products/2/delete")
    json = response.json()
    logger.info(json)
    assert response.status_code == 200

def test_upd_prod():
    prod["name"] = "upded clothing"
    response = client.post("/products/2/delete", json=prod)
    json = response.json()
    logger.info(json)
    assert response.status_code == 200;       



def test_create_store():
    response =  client.post("/stores/new", json=store)
    json = response.json()
    logger.info(json)
    assert response.status_code == 200
    assert json == store

def test_get_store():
    response = client.get("/stores/2/get")
    json = response.json()
    logger.info(json)
    assert response.status_code == 200

def test_del_store():
    response = client.delete("/stores/2/delete")
    json = response.json()
    logger.info(json)
    assert response.status_code == 200

def test_store_prods():
    response = client.get("/stores/2/products")
    json = response.json()
    logger.info(json)
    assert response.status_code == 200

