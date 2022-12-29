from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from chatter.database.base import BaseEntity
from chatter.database.entity.user_chatroom import user_chatroom_entity


class UserEntity(BaseEntity):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True, unique=True, nullable=False)
    full_name = Column(String)
    password_hash = Column(String)

    chatrooms = relationship(
        'ChatroomEntity', secondary=user_chatroom_entity, back_populates='users')
    messages = relationship('MessageEntity', back_populates='sender')
