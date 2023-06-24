from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from jose import jwt, JWTError

from chatter.config import Config
from chatter.dependency.database import get_database
from chatter.database.dao import UserDAO
from chatter.model.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f'{Config.API_PREFIX}/user/token')


def get_user_dao(session: Session = Depends(get_database)) -> UserDAO:
    return UserDAO(session)


def get_current_user(token: str = Depends(oauth2_scheme), dao: UserDAO = Depends(get_user_dao)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, Config.JWT_KEY,
                             algorithms=[Config.JWT_ALGO])

        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = dao.get_user_by_username(username)
    if user is None:
        raise credentials_exception

    return user
