from fastapi import Depends

from sqlalchemy.orm import Session

from chatter.database.dao import MessageDAO
from chatter.dependency.database import get_database


def get_message_dao(session: Session = Depends(get_database)) -> MessageDAO:
    return MessageDAO(session)
