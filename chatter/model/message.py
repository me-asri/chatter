from pydantic import BaseModel, Field
from datetime import datetime


class MessageBase(BaseModel):
    text: str = Field(..., example='Mayushii is my waifu!')


class MessageCreate(MessageBase):
    pass


class Message(MessageCreate):
    id: int
    sender_id: int
    date: datetime

    class Config:
        orm_mode = True
