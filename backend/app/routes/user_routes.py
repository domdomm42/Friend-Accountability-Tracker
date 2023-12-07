from fastapi import APIRouter, HTTPException, Depends, Response
from ..auth.auth_db import register_user
from ..auth.validations import validate_email, validate_password, validate_username, validate_signin
from ..exceptions import InvalidInputException, NotUniqueException
from ..models.user import User, SignIn
from ..helpers import create_access_token, get_current_user
from datetime import timedelta

#the number of minutes issued access token will be valid for
ACCESS_TOKEN_EXPIRE_MINUTES = 60

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

@router.post("/signin")
async def signin_user(response: Response, user: SignIn):
    try:
        #validate the inputted email and password
        await validate_signin(user.email, user.password)
        print("email and password")
    except InvalidInputException as e:
        raise HTTPException(status_code=e.code, detail=e.message)
    
    #create a JWT access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    #set the access token as a cookie
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        secure=False,
        samesite="strict",
    )
    
    return {"message": "Successfully signed in"}

#This route is just here temporarily for testing access tokens
@router.get("/protected", response_model=User)
async def read_users_me(current_user: str = Depends(get_current_user)):
    return current_user

