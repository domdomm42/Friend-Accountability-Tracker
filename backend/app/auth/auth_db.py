from ..models.user import User

async def register_user(user_info: User): 
    await user_info.insert()

async def username_is_unique(username):
    user = await User.find_one(User.username != username)
    return user is not None

async def email_is_unique(email):
    user = await User.find_one(User.email != email)
    return user is not None