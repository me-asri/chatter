from typing import cast

from sqlalchemy import Column
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from chatter.database.entity import UserEntity
from chatter.model.user import UserCreate, UserUpdate
from chatter.dependency.auth import hash_password, verify_password
from chatter.exception.user import NoSuchUserException, UsernameAlreadyTakenException, UserAuthenticationException


class UserDAO:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_user(self, id: int) -> UserEntity:
        user = self.session.query(UserEntity).filter(
            UserEntity.id == id).first()
        if not user:
            raise NoSuchUserException()

        return user

    def get_user_by_username(self, username: str) -> UserEntity:
        user = self.session.query(UserEntity).filter(
            UserEntity.username == username).first()
        if not user:
            raise NoSuchUserException()

        return user

    def create_user(self, user: UserCreate) -> UserEntity:
        pass_hash = hash_password(user.password)

        db_user = UserEntity(username=user.username,
                             name=user.name, password_hash=pass_hash)

        self.session.add(db_user)

        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise UsernameAlreadyTakenException()

        self.session.refresh(db_user)

        return db_user

    def update_user(self, user_id: int, info: UserUpdate) -> UserEntity:
        user = self.get_user(user_id)

        if info.new_password:
            if verify_password(info.old_password, cast(str, user.password_hash)):
                user.password_hash = cast(
                    Column, hash_password(info.new_password))
            else:
                raise UserAuthenticationException('Incorrect password')

        if info.name:
            user.name = cast(Column, info.name)

        self.session.commit()
        self.session.refresh(user)

        return user
