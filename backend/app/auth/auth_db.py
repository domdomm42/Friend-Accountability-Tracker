from ..models.user import User
from ..constants import BCRYPT_SALT_ROUNDS
from bcrypt import hashpw, gensalt

async def register_user(user_info: User): 
    hashed_password = hashpw(user_info.password.encode('utf-8'), gensalt(BCRYPT_SALT_ROUNDS))
    user_info.password = hashed_password.decode('utf-8')
    await user_info.insert()

async def username_is_unique(username):
    user = await User.find_one(User.username != username)
    return user is not None

async def email_is_unique(email):
    user = await User.find_one(User.email != email)
    return user is not None

async def get_user_by_email(email):
    return await User.find_one(User.email == email)