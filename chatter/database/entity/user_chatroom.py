from sqlalchemy import Table, Column, ForeignKey

from chatter.database.base import BaseEntity

user_chatroom_entity = Table(
    'user_chatroom',
    BaseEntity.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('chatroom_id', ForeignKey('chatroom.id'), primary_key=True)
)
