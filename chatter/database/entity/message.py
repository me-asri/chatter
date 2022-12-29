from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from chatter.database.base import BaseEntity


class MessageEntity(BaseEntity):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    sender_id = Column(Integer, ForeignKey('user.id'))
    chatroom_id = Column(Integer, ForeignKey('chatroom.id'))

    sender = relationship('UserEntity', back_populates='messages')
    chatroom = relationship('ChatroomEntity', back_populates='messages')
