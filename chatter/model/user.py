from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(..., example='hikaru')


class UserCreate(UserBase):
    password: str = Field(..., example='password')


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
