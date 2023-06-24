import os


class Config:
    DATABASE_URL = 'sqlite:///./chatterdb.sqlite3'
    API_PREFIX = '/api'

    JWT_KEY = None
    JWT_ALGO = 'HS256'
    JWT_DEFAULT_EXPIRE = 7
