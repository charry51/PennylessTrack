import re
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_version():
    r = client.get("/version")
    assert r.status_code == 200
    data = r.json()
    assert "version" in data
    assert re.match(r"^\d+\.\d+$", str(data["version"]))