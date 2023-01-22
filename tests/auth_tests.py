import httpx
from ..main import app
from fastapi.testclient import TestClient
from ..models.schema import Gender, UserType
from ..common.logger import logger


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