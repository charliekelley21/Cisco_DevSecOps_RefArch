import pytest

from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(app, client):
    res = client.get('/')
    assert res.status_code == 200

def test_gameday(app, client):
    res = client.get("/gameday")
    assert res.status_code == 200

def test_winning(app, client):
    res = client.get("/winning")
    assert res.status_code == 200

