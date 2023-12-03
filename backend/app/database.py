import os
import motor.motor_asyncio
from beanie import init_beanie
from .models.user import User

async def init_db():
    DATABASE_LINK = os.environ.get("DB_LINK")
    DATABASE_NAME = os.environ.get("DB_NAME")
    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_LINK)

    database = client[DATABASE_NAME] 
    await init_beanie(database, document_models=[User])

