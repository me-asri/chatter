from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str = Field(None, example='Hikaru Kawasaki')
    username: str = Field(..., example='hikaru')


class UserCreate(UserBase):
    password: str = Field(..., example='password')


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
