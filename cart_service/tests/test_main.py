from fastapi.testclient import TestClient
from cart_service.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al cart_service"}

def test_get_cart_empty_user():
    response = client.get("/cart/9999")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
