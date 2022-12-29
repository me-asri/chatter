from pydantic import BaseModel, Field


class MessageBase(BaseModel):
    text: str = Field(..., example='Mayushii is my waifu!')


class MessageCreate(MessageBase):
    chatroom_id: int


class Message(MessageCreate):
    id: int

    sender_id: int

    class Config:
        orm_mode = True


# from chatter.model.user import User  # nopep8
# from chatter.model.chatroom import Chatroom  # nopep8
# Message.update_forward_refs()
