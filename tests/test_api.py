from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_sort_endpoint_basic():
    resp = client.post('/sort', json={'numbers': [0, 1, 2, 3, 4, 5]})
    assert resp.status_code == 200
    assert resp.json()['sorted_numbers'] == [0, 1, 2, 4, 3, 5]


def test_sort_endpoint_invalid_input():
    resp = client.post('/sort', json={'numbers': ['a', 2]})
    assert resp.status_code == 422
