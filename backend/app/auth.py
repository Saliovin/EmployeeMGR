import os
import time
import bcrypt
import jwt
from fastapi import Cookie, HTTPException

JWT_SECRET = os.getenv("JWT_SECRET", "58b5dad53d404dc19d4fcd37e22b4cdb")


def generate_jwt(user: str):
    payload = {"user": user, "exp": time.time() + 7200}

    return jwt.encode(payload, JWT_SECRET)


def verify_jwt(token: str):
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    return decoded_token


def is_pass_valid(password: bytes, hashed_password: bytes):
    return bcrypt.checkpw(password, hashed_password)


def verify_token(token: str = Cookie()):
    try:
        verify_jwt(token)
    except Exception:
        raise HTTPException(status_code=400, detail="Token invalid")
