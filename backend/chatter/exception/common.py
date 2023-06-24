from typing import Any

from fastapi import HTTPException, status


class InvalidQueryException(HTTPException):
    def __init__(self, detail: str = 'Invalid query parameters') -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail)
