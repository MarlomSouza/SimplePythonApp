from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_env():
    r = client.get("/env")
    assert r.status_code == 200
    # Should contain at least one env var (PATH likely)
    assert isinstance(r.json(), dict)
    assert len(r.json()) > 0

def test_time():
    r = client.get("/time")
    assert r.status_code == 200
    body = r.json()
    assert "utc_time" in body
    assert body["utc_time"].endswith("Z") or body["utc_time"].endswith("+00:00")
