#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "9848283"
API_HASH = "c4e36306a2c11dab87bcc8826cba7fc7"
BOT_TOKEN = "5851916195:AAHqhPfhr_fEnsJ03Ch6-jZM6l8hsO8cJaY"
SESSION = "BQDABItrPdqBx_csTY3gePWWR6PHUncNv2I1UzmIcGpFFRUbqfLYZKZ0pSCQTmI8RzJsrO-uy8pwhxNzZFL1g2sQchPI5u-N5vf5xmcM8tVkOXvcfZZ3R4rdYleK7exVCcKUZdt0jzcxumrUChoBnSUvn1eII5TCiz1jjIRWRy3QKzCF_qrtjXxOzzcz_kQ6LI5RYCmGXfFvYQDemb6kA8zVbji8aS2oVN46IsctSP6nokRUCKOBFVBmdfthCFEWrWODl3XdhFPwfSWBAjS_uAOUg6LWlVNJGey2VSofO2IHLnCjMIVnqJzcF2gPF-b8Gk9LanJuglO5LnzSRgnbwwa2c5MdwgA"
FORCESUB = "sedotkuy"
AUTH = 1939021250

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
