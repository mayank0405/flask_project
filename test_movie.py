import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Movie Review API!" in response.data

def test_add_review(client):
    response = client.post("/reviews", json={"title": "Inception", "review": "Amazing movie!"})
    assert response.status_code == 201
    assert response.json["message"] == "Review added successfully"

def test_get_reviews(client):
    client.post("/reviews", json={"title": "Inception", "review": "Amazing movie!"})
    response = client.get("/reviews")
    assert response.status_code == 200
    assert len(response.json) > 0
    assert response.json[0]["title"] == "Inception"
    assert response.json[0]["review"] == "Amazing movie!"
