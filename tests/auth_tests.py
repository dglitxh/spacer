import httpx
from ..main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_signup():
    response = client.get("/signup")
    assert response.status_code == 200