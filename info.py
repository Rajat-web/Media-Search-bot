import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Admins & Channels
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(channel) if re.search('^-100\d+$', channel) else channel for channel in environ['CHANNELS'].split()]

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """<b>Hi {}!</b>\n<b>I'm a simple inline app searching bot which helps you to search and share applications and softwares.</b>\n<b>Hit the go inline button or call me from any chat just by typing my username in the text field.</b>\n<b>NB: Make sure the name of the app you are looking for is correct else bot cannot index it while searching.</b>""""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
