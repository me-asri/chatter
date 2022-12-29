from chatter.secret import Secret


class Config:
    DATABASE_URL = 'sqlite:///./chatterdb.sqlite3'
    STATIC_FILES_DIR = 'static'
    API_PREFIX = '/api'

    JWT_KEY = Secret.JWT_KEY  # can be generated using `openssl rand -hex 32`
    JWT_ALGO = 'HS256'
    JWT_DEFAULT_EXPIRE = 7
