import httpx
from ..main import app
from fastapi.testclient import TestClient
from ..common.logger import logger
from common.db import rdb

client = TestClient(app)

creds = {
    "id": 322,
    "firstname": "da",
    "lastname": "boii",
    "age": 29,
    "email": "daboii@m.com",
    "gender": "male",
    "password": "daabodaabo",
    "user_type": "admin"
}
def test_signup():
    response =  client.post("/auth/signup", json=creds)
    json = response.json()
    logger.info(json)
    assert response.status_code == 200
    assert json == creds

def test_signin():
    response = client.post("/auth/login", json={"email": "daboii@m.com", "password":"daabodaabo"})
    json = response.json()
    assert response.status_code == 200
    assert json == creds

token = rdb.get("token")

def test_get_user(token):
    response = client.get("/auth/user")
    json = response.json()
    assert response.status_code == 200
    assert json.email == "daboii@m.com"
