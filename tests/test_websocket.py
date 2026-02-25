import json

from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_websocket_sort_basic():
    with client.websocket_connect('/ws') as ws:
        payload = {"numbers": [0, 1, 2, 3, 4, 5]}
        ws.send_text(json.dumps(payload))
        data = ws.receive_json()
        assert data.get('sorted_numbers') == [0, 1, 2, 4, 3, 5]
