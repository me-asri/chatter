from typing import List
from sqlalchemy.orm import Session

from chatter.database.entity import ChatroomEntity, UserEntity
from chatter.model.chatroom import ChatroomCreate
from chatter.model.user import User
from chatter.exception.chatroom import NoSuchChatroomException, UserAlreadyInChatroomException, UserNotInChatroomException


class ChatroomDAO:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_chatroom(self, chatroom_id: int) -> ChatroomEntity:
        chatroom = self.session.query(ChatroomEntity).filter(
            ChatroomEntity.id == chatroom_id).first()
        if not chatroom:
            raise NoSuchChatroomException()

        return chatroom

    def get_chatrooms_for_user(self, user: User) -> List[ChatroomEntity]:
        return self.session.query(ChatroomEntity).filter(ChatroomEntity.users.any(UserEntity.id == user.id)).all()

    def create_chatroom(self, chatroom: ChatroomCreate, user: User) -> ChatroomEntity:
        db_chatroom = ChatroomEntity(name=chatroom.name)
        db_chatroom.users.append(user)

        self.session.add(db_chatroom)
        self.session.commit()
        self.session.refresh(db_chatroom)

        return db_chatroom

    def join_chatroom(self, chatroom_id: int, user: User) -> None:
        db_chatroom = self.get_chatroom(chatroom_id)
        if not db_chatroom:
            raise NoSuchChatroomException()

        if user in db_chatroom.users:
            raise UserAlreadyInChatroomException()

        db_chatroom.users.append(user)
        self.session.commit()

    def leave_chatroom(self, chatroom_id: int, user: User) -> None:
        db_chatroom = self.get_chatroom(chatroom_id)
        if not db_chatroom:
            raise NoSuchChatroomException()

        if user not in db_chatroom.users:
            raise UserNotInChatroomException()

        db_chatroom.users.remove(user)

        # Remove chatroom completely if no users exist in it
        if not db_chatroom.users:
            self.session.delete(db_chatroom)

        self.session.commit()
