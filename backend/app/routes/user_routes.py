from fastapi import APIRouter, HTTPException
from ..auth.auth_db import register_user
from ..exceptions import InvalidInputException, NotUniqueException
from ..models.user import User
from ..auth.validations import validate_email, validate_password, validate_username

router = APIRouter()

@router.get("/")
async def display_info():
    return "hello"

@router.post("/signup")
async def signup_user(user: User):
    try:
        await validate_username(user.username)
        print("username")
        await validate_email(user.email)
        print("email")
        await validate_password(user.username, user.password)
        print("password")
    except InvalidInputException as e:
        raise HTTPException(status_code=e.code, detail=e.message)
    except NotUniqueException as e:
        raise HTTPException(status_code=e.code, detail=e.message)
    
    await register_user(user)
    return {}