import os

class Config(object):
    SECRET_KEY = os.environ.get('dev') or 'you-will-never-guess'
