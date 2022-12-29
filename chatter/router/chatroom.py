from typing import List
from fastapi import APIRouter, Depends

from chatter.tag import Tag
from chatter.model.chatroom import ChatroomOut, ChatroomCreate, Chatroom
from chatter.model.user import User
from chatter.dependency.user import get_current_user
from chatter.dependency.chatroom import get_chatroom_dao
from chatter.database.dao import ChatroomDAO

router = APIRouter(
    prefix='/chatroom',
    tags=[Tag.CHATROOM]
)


@router.get(
    '/',
    summary='Get chatrooms the user has joined',
    response_model=List[ChatroomOut]
)
def get_chatrooms_for_user(user=Depends(get_current_user), dao: ChatroomDAO = Depends(get_chatroom_dao)):
    return dao.get_chatrooms_for_user(user)


@router.post(
    '/',
    summary='Create a new chatroom',
    response_model=ChatroomOut
)
def create_chatroom(chatroom: ChatroomCreate, creator: User = Depends(get_current_user), dao: ChatroomDAO = Depends(get_chatroom_dao)):
    return dao.create_chatroom(chatroom, creator)


@router.get(
    '/{id}',
    summary='Get chatroom information',
    response_model=Chatroom
)
def get_chatroom_info(id: int, dao: ChatroomDAO = Depends(get_chatroom_dao)):
    return dao.get_chatroom(id)


@router.put(
    '/{id}',
    summary='Join a chatroom',
    response_model=List[ChatroomOut]
)
def join_chatroom(id: int, user: User = Depends(get_current_user), dao: ChatroomDAO = Depends(get_chatroom_dao)):
    dao.join_chatroom(id, user)
    return dao.get_chatrooms_for_user(user)


@router.delete(
    '/{id}',
    summary='Leave a chatroom',
    response_model=List[ChatroomOut]
)
def delete_chatroom(id: int, user: User = Depends(get_current_user), dao: ChatroomDAO = Depends(get_chatroom_dao)):
    dao.leave_chatroom(id, user)
    return dao.get_chatrooms_for_user(user)
