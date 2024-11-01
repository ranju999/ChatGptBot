from os import environ

# bot
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# database

DATABASE_URL = environ.get('DATABASE_URL', '')
