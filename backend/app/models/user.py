from beanie import Document
from pydantic import BaseModel

class User(Document):
    username: str
    email: str
    password: str
    

class SignIn(BaseModel):
    email: str
    password: str