import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["message"] == "Hello from Capstone Flask API!"

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json["status"] == "healthy"
