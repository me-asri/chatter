from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from chatter.database.base import BaseEntity


class MessageEntity(BaseEntity):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    date = Column(DateTime, server_default=func.now())
    sender_id = Column(Integer, ForeignKey('user.id'))

    sender = relationship('UserEntity', back_populates='messages')
