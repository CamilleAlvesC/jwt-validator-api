# tests/test_validate.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

TOKENS = {
    "case1_true": "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJTZWVkIjoiNzg0MSIsIk5hbWUiOiJUb25pbmhvIEFyYXVqbyJ9.QY05sIjtrcJnP533kQNk8QXcaleJ1Q01jWY_ZzIZuAg",
    "case2_false": "eyJhbGciOiJzI1NiJ9.dfsdfsfryJSr2xrIjoiQWRtaW4iLCJTZrkIjoiNzg0MSIsIk5hbrUiOiJUb25pbmhvIEFyYXVqbyJ9.QY05fsdfsIjtrcJnP533kQNk8QXcaleJ1Q01jWY_ZzIZuAg",
    "case3_false": "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiRXh0ZXJuYWwiLCJTZWVkIjoiODgwMzciLCJOYW1lIjoiTTRyaWEgT2xpdmlhIn0.6YD73XWZYQSSMDf6H0i3-kylz1-TY_Yt6h1cV2Ku-Qs",
    "case4_false": "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiTWVtYmVyIiwiT3JnIjoiQlIiLCJTZWVkIjoiMTQ2MjciLCJOYW1lIjoiVmFsZGlyIEFyYW5oYSJ9.cmrXV_Flm5mfdpfNUVopY_I2zeJUy4EZ4i3Fea98zvY",
}

def test_case1_true():
    r = client.get("/validate", params={"token": TOKENS["case1_true"]})
    assert r.status_code == 200
    assert r.json() == {"valido": True}

def test_case2_false():
    r = client.get("/validate", params={"token": TOKENS["case2_false"]})
    assert r.status_code == 200
    assert r.json() == {"valido": False}

def test_case3_false():
    r = client.get("/validate", params={"token": TOKENS["case3_false"]})
    assert r.status_code == 200
    assert r.json() == {"valido": False}

def test_case4_false():
    r = client.get("/validate", params={"token": TOKENS["case4_false"]})
    assert r.status_code == 200
    assert r.json() == {"valido": False}