from os import getenv
import re
from jwt import encode, decode, InvalidTokenError, DecodeError, ExpiredSignatureError
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends, Cookie
from fastapi.security import OAuth2PasswordBearer
from .auth.auth_db import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")

def is_email(email: str) -> bool:
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_regex, email) is not None

## creates JWT access tokens
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    secret_key = getenv("JWT_SECRET")
    if not secret_key:
        raise Exception("JWT_SECRET is not set in the environment variables")
    encoded_jwt = encode(to_encode, secret_key, algorithm="HS256")
    return encoded_jwt

#verifies the JWT access token
def verify_token(token: str) -> dict:
    secret_key = getenv("JWT_SECRET")
    if not secret_key:
        raise Exception("JWT_SECRET is not set in the environment variables")
    try:
        decoded_token = decode(token, secret_key, algorithms=["HS256"])
    except DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
        )
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token has expired",
        )
    except InvalidTokenError:
        raise Exception("Invalid token")
    return decoded_token

#gets the current user from the access token
async def get_current_user(access_token: str = Cookie(None)):
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    payload = verify_token(access_token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    email = payload.get("sub")
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await get_user_by_email(email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user