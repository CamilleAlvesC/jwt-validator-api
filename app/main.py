# app/main.py
from fastapi import FastAPI, Query
import jwt

app = FastAPI(title="JWT Validator API", version="1.0.0")

ALLOWED_ROLES = {"Admin", "Member", "External"}

def is_prime(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0: return n == 2
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

@app.get("/validate")
def validate_jwt(token: str = Query(...)):
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
    except Exception:
        return {"valido": False}
    
    if set(payload.keys()) != {"Name", "Role", "Seed"}:
        return {"valido": False}
    
    name = payload.get("Name")
    if not isinstance(name, str) or len(name) > 256 or any(ch.isdigit() for ch in name):
        return {"valido": False}
    
    role = payload.get("Role")
    if role not in ALLOWED_ROLES:
        return {"valido": False}
    
    try:
        seed = int(payload.get("Seed"))
    except:
        return {"valido": False}
    
    if not is_prime(seed):
        return {"valido": False}
    
    return {"valido": True}

@app.get("/decode")
def decode_only(token: str = Query(...)):
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
        return {"claims": payload}
    except:
        return {"erro": "JWT inválido"}
