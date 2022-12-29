from typing import Any

from fastapi import HTTPException, status


class ChatroomException(HTTPException):
    def __init__(self, status_code: int, detail: Any = None) -> None:
        super().__init__(status_code, detail)


class NoSuchChatroomException(ChatroomException):
    def __init__(self, detail: str = 'No such chatroom exists') -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail)


class UserAlreadyInChatroomException(ChatroomException):
    def __init__(self, detail: str = 'User already in chatroom') -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail)


class UserNotInChatroomException(ChatroomException):
    def __init__(self, detail: str = 'User not in chatroom') -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail)
