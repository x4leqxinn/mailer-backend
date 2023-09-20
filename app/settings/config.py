from decouple import config
from .openapi import *


APP_HOST = config('APP_HOST')
APP_PORT = config('APP_PORT',cast=int)

TIMEZONE = 'Chile/Continental'


ALLOW_ORIGINS = ['http://0.0.0.0:8000']
ALLOW_CREDENTIALS = True
ALLOW_METHODS = ['*']
ALLOW_HEADERS = ['*']
EXPOSE_HEADERS = ''


# MAILER
MAILER_SERVER = config('MAILER_SERVER',cast=str)
MAILER_PORT = config('MAILER_PORT',cast=int)
MAILER_HOST = config('MAILER_HOST',cast=str)
MAILER_PASSWORD = config('MAILER_PASSWORD',cast=str)

