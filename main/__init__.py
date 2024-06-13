#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# variables
API_ID = "10577882" #config("API_ID", default=None, cast=int)
API_HASH = "5ab4593a5f6c59a96b9abafdc7f08943" #config("API_HASH", default=None)
BOT_TOKEN = "7368437982:AAFQ4fFnT_50GLM9Aap-aw3ZOv6zn8yO9oQ" #config("BOT_TOKEN", default=None)
SESSION = "BQChZ9oANCcUTcKEVVMKOtKqUOLdMjF9ySyV8da5wngRJxDLjOtNVB06p5tMh9oWMoa5Dkpuqek7piSnbhsjxzF3NHLDxK3bj1X7PThULPOGZR4tpEqsaww3_8DqM67iaW33u8f3jtYMDjKgdGxXKLpe0uFyotW3mzeiT-j86elmNVgZ6s4gjywfDLfpIqblhcvo8Sl8tV75DIeUe_rkpaSmxHu1qkRphBfddI0ozVQFEUdUopNb2DV8IqqMkzOIQUuVVy70M45bsyGjBt6sFT5-60e8907hry2KiKadb4VTPhuNSb0pOlcUsqBFLFVoOM-oVuyqwnLeVBOmwkNjvA2iRvKZJwAAAABo7yz4AA" #config("SESSION", default=None)
FORCESUB = #config("FORCESUB", default=None)
AUTH = "10577882" #config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
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
    # print(e)
    # logger.info(e)
    sys.exit(1)
