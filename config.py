from os import environ
import re

id_pattern = re.compile(r'^.\d+$')

# bot
API_ID = int(environ.get('API_ID', '12380656'))
API_HASH = environ.get('API_HASH', 'd927c13beaaf5110f25c505b7c071273')
BOT_TOKEN = environ.get('BOT_TOKEN', '7232006758:AAGV-HPIfJi3k-gz2_YR6_-1k7706NEPD-I')
ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in environ.get('ADMINS', '5977931010').split()]

# bs
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '2114619001'))
fsub_eid = environ.get('FSUB_ID')
FSUB_ID = int(fsub_eid) if fsub_eid and id_pattern.search(fsub_eid) else None

# database

DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://aman727587:aman@cluster0.bk39x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
