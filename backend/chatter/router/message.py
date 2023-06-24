from typing import List

from fastapi import APIRouter, Depends, Query

from chatter.tag import Tag
from chatter.model.user import User
from chatter.model.message import MessageCreate, Message
from chatter.database.dao import MessageDAO
from chatter.dependency.user import get_current_user
from chatter.dependency.message import get_message_dao
from chatter.exception.common import InvalidQueryException

router = APIRouter(
    prefix='/message',
    tags=[Tag.MESSAGE]
)


@router.post(
    '/',
    summary='Post a new message',
    response_model=Message
)
def post_message(message: MessageCreate, user: User = Depends(get_current_user), msgdao: MessageDAO = Depends(get_message_dao)):
    return msgdao.create_message(message, user)


@router.get(
    '/',
    summary='Get messages',
    response_model=List[Message]
)
def get_messages(
    msgdao: MessageDAO = Depends(get_message_dao),
    limit: int = Query(10, description='Max number of messages to fetch'),
    since: int = Query(None, description='Last message ID'),
    until: int = Query(None, description='Last message ID')
):
    if since and until:
        raise InvalidQueryException(
            "'since' and 'until' parameters are mutually exclusive")

    if until != None:
        return msgdao.get_messages_until(until, limit)
    else:
        if since == None:
            since = -1
        return msgdao.get_messages(limit, since)
