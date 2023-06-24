from typing import List

from sqlalchemy.orm import Session

from chatter.database.entity import MessageEntity
from chatter.model.message import MessageCreate
from chatter.model.user import User
from chatter.exception.message import NoSuchMessageException


class MessageDAO:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_message(self, message_id: int) -> MessageEntity:
        message = self.session.query(MessageEntity).filter(
            MessageEntity.id == message_id).first()
        if not message:
            raise NoSuchMessageException()

        return message

    def create_message(self, message: MessageCreate, sender: User) -> MessageEntity:
        db_message = MessageEntity(
            text=message.text, sender_id=sender.id)

        self.session.add(db_message)
        self.session.commit()
        self.session.refresh(db_message)

        return db_message

    def get_messages(self, limit: int = 10, since: int = -1) -> List[MessageEntity]:
        return self.session.query(MessageEntity).order_by(MessageEntity.id.desc()).filter(MessageEntity.id > since).limit(limit).all()[::-1]

    def get_messages_until(self, until: int, limit: int = 10) -> List[MessageEntity]:
        return self.session.query(MessageEntity).order_by(MessageEntity.id.desc()).filter(MessageEntity.id < until).limit(limit).all()[::-1]
