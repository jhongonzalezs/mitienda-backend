from fastapi.testclient import TestClient
from category_service.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al category_service"}

def test_get_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
