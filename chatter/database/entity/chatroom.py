from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from chatter.database.base import BaseEntity
from chatter.database.entity.user_chatroom import user_chatroom_entity


class ChatroomEntity(BaseEntity):
    __tablename__ = 'chatroom'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    users = relationship(
        'UserEntity', secondary=user_chatroom_entity, back_populates='chatrooms')
    messages = relationship('MessageEntity', back_populates='chatroom')
