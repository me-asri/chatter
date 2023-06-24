from typing import Any

from fastapi import HTTPException, status


class UserException(HTTPException):
    def __init__(self, status_code: int, detail: Any = None) -> None:
        super().__init__(status_code, detail)


class NoSuchUserException(UserException):
    def __init__(self, detail: str = 'No such user exists') -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail)


class UsernameAlreadyTakenException(UserException):
    def __init__(self, detail: str = 'Username already taken') -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail)


class UserAuthenticationException(UserException):
    def __init__(self, detail: str = 'Incorrent username and/or password') -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail)


class UnauhtorizedUserException(UserException):
    def __init__(self, detail: str = 'Unauthorized') -> None:
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail)
