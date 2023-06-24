from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from chatter.config import Config
from chatter.router import user, message
from chatter.database.base import create_database

create_database()

app = FastAPI(
    title='Chatter API',
    openapi_url=f'{Config.API_PREFIX}/openapi.json',
    docs_url=f'{Config.API_PREFIX}/docs',
    redoc_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(user.router, prefix=Config.API_PREFIX)
app.include_router(message.router, prefix=Config.API_PREFIX)
