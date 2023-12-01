from beanie import Document

class User(Document):
    username: str
    email: str
    password: str
    
    