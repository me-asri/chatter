from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(..., example='hikaru')
    full_name: str = Field(None, example='Hikaru Azai')


class UserCreate(UserBase):
    password: str = Field(..., example='password')


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
