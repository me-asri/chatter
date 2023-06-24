from typing import Union
from datetime import datetime, timedelta

from chatter.config import Config

from jose import jwt

from passlib.context import CryptContext

pass_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    return pass_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return pass_context.verify(password, hash)


def create_access_token(username: str, expire_data: Union[timedelta, None] = None) -> str:
    if expire_data:
        expire = datetime.utcnow() + expire_data
    else:
        expire = datetime.utcnow() + timedelta(days=Config.JWT_DEFAULT_EXPIRE)

    data = {
        "exp": expire,
        "sub": username
    }
    encoded_jwt = jwt.encode(data, Config.JWT_KEY, algorithm=Config.JWT_ALGO)
    return encoded_jwt
