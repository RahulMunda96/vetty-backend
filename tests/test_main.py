from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token():
    r = client.post("/token", json={"username": "admin", "password": "admin123"})
    return r.json()["access_token"]

def test_health():
    assert client.get("/health").status_code == 200

def test_auth_and_coins():
    token = get_token()
    r = client.get("/coins", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
