from enum import Enum


class Tag(str, Enum):
    USER = 'user'
    CHATROOM = 'chatroom'
    MESSAGE = 'message'
