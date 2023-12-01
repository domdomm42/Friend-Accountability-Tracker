from . import auth_db
from ..exceptions import InvalidInputException, NotUniqueException
from pyhibp import pwnedpasswords as pw
from ..helpers import is_email
from .. import constants as c

import pyhibp

async def validate_username(username: str) -> None:

    # check username length
    if not username or not (c.MIN_USERNAME_LEN <= len(username) <= c.MAX_USERNAME_LEN):
        raise InvalidInputException(
            f"Username must be between {c.MIN_USERNAME_LEN} and {c.MAX_USERNAME_LEN} characters in length."
        )

    # check if username
    if not username.isalnum():
        raise InvalidInputException("Username must contian only alpha-numeric characters.")

    # check if username is unique
    if not await auth_db.username_is_unique(username):
        raise NotUniqueException(f"Username '{username}' is already taken.")


async def validate_email(email: str) -> None:
    if not email or not is_email(email):
        raise InvalidInputException("Invalid email syntax.")

    if not await auth_db.email_is_unique(email):
        raise NotUniqueException(f"The email {email} is already associated with an account.")


async def validate_password(username: str, password: str) -> None:
    if not password or not (c.MIN_PASSWORD_LEN <= len(password) <= c.MAX_USERNAME_LEN):
        raise InvalidInputException(
            f"Passwords must be between {c.MIN_PASSWORD_LEN} and {c.MAX_USERNAME_LEN} characters in length."
        )

    # Check if password contains the username
    if username in password:
        raise InvalidInputException("Password must not include the username.")

    # Check if password has been breached
    pyhibp.set_user_agent(ua="friendo")
    if pw.is_password_breached(password):
        raise InvalidInputException("This password has been breached online. Please choose another password.")

    if len(username) >= c.INVALID_USERNAME_PASSWORD_SUBSTR_LEN:
        for i in range(len(password) - c.INVALID_USERNAME_PASSWORD_SUBSTR_LEN):
            substring = password[i : i + c.INVALID_USERNAME_PASSWORD_SUBSTR_LEN + 1]
            if substring in username:
                raise InvalidInputException("Password cannot contain a substring of username.")
