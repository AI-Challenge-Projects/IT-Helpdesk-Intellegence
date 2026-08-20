from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_valid_ticket():
    response = client.post("/predict", json={"ticket_text": "my laptop won't turn on"})
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "Hardware"
    assert data["routed_team"] == "Desktop Support"

def test_predict_missing_text_returns_422():
    response = client.post("/predict", json={})
    assert response.status_code == 422