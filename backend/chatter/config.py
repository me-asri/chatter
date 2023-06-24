import os


class Config:
    API_PREFIX = '/api'

    JWT_KEY = None
    JWT_ALGO = 'HS256'
    JWT_DEFAULT_EXPIRE = 7
