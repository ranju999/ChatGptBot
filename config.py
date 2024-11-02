from os import environ
import re

id_pattern = re.compile(r'^.\d+$')

# bot
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in environ.get('ADMINS', '1867106198').split()]

# bs
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))


# database

DATABASE_URL = environ.get('DATABASE_URL', '')
