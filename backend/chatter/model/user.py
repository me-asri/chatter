from pydantic import BaseModel, Field, validator

import re


class UserBase(BaseModel):
    name: str = Field(None, example='Hikaru Kawasaki')
    username: str = Field(..., example='hikaru')

    @validator('name')
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value:
            return value

        name = re.sub(r'\s+', ' ', value)

        if len(name) > 30:
            raise ValueError('Name is too long')
        return name

    @validator('username')
    @classmethod
    def validate_username(cls, value: str) -> str:
        if len(value) < 4:
            raise ValueError('Username too short')
        if len(value) > 16:
            raise ValueError('Username too long')
        if not re.match(r'^[a-z0-9]+$', value):
            raise ValueError('Only a-z, 0-9 allowed in username')

        return value


class UserCreate(UserBase):
    password: str = Field(..., example='password')

    @validator('password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError('Password too short')
        return value


class UserUpdate(BaseModel):
    name: str = Field(None, example='Hikaru Azai')
    old_password: str = Field(None, example='password')
    new_password: str = Field(None, example='new password')

    @validator('name')
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value:
            return value

        name = re.sub(r'\s+', ' ', value)

        if len(name) > 30:
            raise ValueError('Name is too long')
        return name

    @validator('old_password', 'new_password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        if not value:
            return value

        if len(value) < 8:
            raise ValueError('Password too short')
        return value


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
