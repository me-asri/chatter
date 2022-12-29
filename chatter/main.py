from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from chatter.config import Config
from chatter.router import user, chatroom, message
from chatter.database.base import create_database

create_database()

app = FastAPI(
    title='Chatter API',
    openapi_url=f'{Config.API_PREFIX}/openapi.json',
    docs_url=f'{Config.API_PREFIX}/docs',
    redoc_url=None
)

app.include_router(user.router, prefix=Config.API_PREFIX)
app.include_router(chatroom.router, prefix=Config.API_PREFIX)
app.include_router(message.router, prefix=Config.API_PREFIX)

app.mount('/', StaticFiles(directory=Config.STATIC_FILES_DIR,
          html=True), name='static')
