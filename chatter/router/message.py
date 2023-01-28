from fastapi import APIRouter, Depends

from chatter.tag import Tag
from chatter.model.user import User
from chatter.model.message import MessageCreate, Message
from chatter.database.dao import MessageDAO
from chatter.dependency.user import get_current_user
from chatter.dependency.message import get_message_dao

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
