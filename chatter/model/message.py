from datetime import datetime

from pydantic import BaseModel, Field

from chatter.model.user import User


class MessageBase(BaseModel):
    text: str = Field(..., example='Mayushii is my waifu!')


class MessageCreate(MessageBase):
    pass


class Message(MessageCreate):
    id: int
    date: datetime
    sender: User

    class Config:
        orm_mode = True
