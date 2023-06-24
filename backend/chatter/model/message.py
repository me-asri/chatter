from datetime import datetime
from datetime import timezone

from pydantic import BaseModel, Field, validator

from chatter.model.user import User


class MessageBase(BaseModel):
    text: str = Field(..., example='Mayushii is my waifu!')

    @validator('text')
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()

        if len(value) < 1:
            raise ValueError('Message cannot be empty')

        return value


class MessageCreate(MessageBase):
    pass


class Message(MessageCreate):
    id: int
    date: datetime
    sender: User

    class Config:
        orm_mode = True

        json_encoders = {
            datetime: lambda date: date.replace(
                tzinfo=timezone.utc).timestamp()
        }
