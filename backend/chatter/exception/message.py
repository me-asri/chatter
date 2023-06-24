from typing import Any

from fastapi import HTTPException, status


class MessageException(HTTPException):
    def __init__(self, status_code: int, detail: Any = None) -> None:
        super().__init__(status_code, detail)


class NoSuchMessageException(MessageException):
    def __init__(self, detail: str = 'No such message exists') -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail)
