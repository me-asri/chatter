from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from chatter.database.entity import UserEntity
from chatter.model.user import UserCreate
from chatter.dependency.auth import hash_password
from chatter.exception.user import NoSuchUserException, UsernameAlreadyTakenException


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
