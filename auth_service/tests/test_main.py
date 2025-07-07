from fastapi.testclient import TestClient
from auth_service.main import app 

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al auth_service"}

def test_create_user():
    response = client.post("/users", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code in [200, 400] 

def test_login_user():
    response = client.post("/users/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code in [200, 401]
