from fastapi import Depends

from sqlalchemy.orm import Session

from chatter.dependency.database import get_database
from chatter.database.dao import ChatroomDAO


def get_chatroom_dao(session: Session = Depends(get_database)) -> ChatroomDAO:
    return ChatroomDAO(session)
