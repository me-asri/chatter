import os

import uvicorn

from chatter.config import Config

try:
    Config.JWT_KEY = os.environ['CHATTER_SECRET']
except KeyError:
    print('CHATTER_SECRET environment variable is not defined. You can generate a key using `openssl rand -hex 32`')
    exit(1)

db_dir = os.environ.get('CHATTER_DB_DIR', '.')
Config.DATABASE_URL = f'sqlite:///{db_dir}/chatterdb.sqlite3'

host = os.environ.get('CHATTER_IP', '0.0.0.0')
port = os.environ.get('CHATTER_PORT', '8000')

uvicorn.run(
    "chatter.main:app",
    host=host,
    port=int(port),
    reload=False
)
