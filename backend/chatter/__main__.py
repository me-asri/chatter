import os

import uvicorn

from chatter.config import Config

host = os.environ.get('CHATTER_IP', '0.0.0.0')
port = os.environ.get('CHATTER_PORT', '8000')

try:
    Config.JWT_KEY = os.environ['CHATTER_SECRET']
except KeyError:
    print('CHATTER_SECRET environment variable is not defined. You can generate a key using `openssl rand -hex 32`')
    exit(1)

uvicorn.run(
    "chatter.main:app",
    host=host,
    port=int(port),
    reload=False
)
