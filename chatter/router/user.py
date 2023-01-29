from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from chatter.tag import Tag
from chatter.model.user import User, UserCreate, UserUpdate
from chatter.dependency.auth import create_access_token, verify_password
from chatter.dependency.user import get_current_user, get_user_dao
from chatter.database.dao import UserDAO
from chatter.exception.user import NoSuchUserException, UserAuthenticationException

router = APIRouter(
    prefix='/user',
    tags=[Tag.USER]
)


@router.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends(), dao: UserDAO = Depends(get_user_dao)):
    try:
        user = dao.get_user_by_username(form_data.username)
    except NoSuchUserException:
        raise UserAuthenticationException()

    if not verify_password(form_data.password, str(user.password_hash)):
        raise UserAuthenticationException()

    return {"access_token": create_access_token(str(user.username)), "token_type": "bearer"}


@router.post(
    '/',
    summary='Create a new user',
    response_model=User
)
def create_user(user: UserCreate, dao: UserDAO = Depends(get_user_dao)) -> User:
    return dao.create_user(user)


@router.put(
    '/',
    summary='Update user information',
    response_model=User
)
def update_user(info: UserUpdate, user: User = Depends(get_current_user), dao: UserDAO = Depends(get_user_dao)):
    return dao.update_user(user.id, info)


@router.get(
    '/me',
    summary='Get current user information',
    response_model=User
)
def get_user_me(user: User = Depends(get_current_user)):
    return user
