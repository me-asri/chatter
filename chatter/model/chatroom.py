from typing import List
from pydantic import BaseModel, Field


class ChatroomBase(BaseModel):
    name: str = Field(..., example='Anime Club')


class ChatroomCreate(ChatroomBase):
    pass


class ChatroomOut(ChatroomBase):
    id: int

    class Config:
        orm_mode = True


class Chatroom(ChatroomOut):
    users: 'List[User]'
    messages: 'List[Message]'

    class Config:
        orm_mode = True


from chatter.model.user import User  # nopep8
from chatter.model.message import Message  # nopep8
Chatroom.update_forward_refs()
