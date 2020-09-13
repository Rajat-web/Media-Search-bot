import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Admins & Channels
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(channel) if re.search('^-100\d+$', channel) else channel for channel in environ['CHANNELS'].split()]

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
**Hi {}, I'm Modzilla Apk Bot**

Here You Can Search Files In Inline Mode. Just Press Follwing Buttons And Start Searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
