from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from chatter.database.base import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True, unique=True, nullable=False)
    name = Column(String)
    password_hash = Column(String)

    messages = relationship('MessageEntity', back_populates='sender')
