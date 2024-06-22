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

uvloop.install()
MDB = "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn"
API_ID = "27815405" #config("API_ID", default=None, cast=int)
API_HASH = "4e70821cd2af3322f7cf2f2887e32821" #config("API_HASH", default=None)
BOT_TOKEN = "7231166671:AAF2-bSCPm9xH8KyjtUZChxkkOpX_sCrUHM" #config("BOT_TOKEN", default=None)
SESSION = "BQGobe0AT7MCMoLbHhonlFYkEqm6_DGND8HW2qzCmG1Dhc7YsB38duNBTHVncgOzicpIShuh48yEPfkodn_M1EPsBgNJ-ON508t-M1R7eGpCvEcCiYR6HgVti0KaR7KekFNm40Wbd7QsHuG9Fc86OEVxp7sk9SR8hIVMCXCPuGF49Sypf1Sn5kecmuby8As3GsqviB-W8oPtGgPRJw2CVDkeUlBRbVeof1B7HfSN2eriqX-WnNrhttXUInyrn8jEDaegTvUiuL_mtaX8uSpVBVMFf8ImSATpHmIFNI5abfaU0UeOoVVtcYkM4We2tKlObG2ROrU2xtE5C3-aKCdV01hI9Bh8qwAAAAGOJFsyAA" #config("SESSION", default=None)
FORCESUB = "SmexyStore" #config("FORCESUB", default=None)
AUTH = "6679714610" #config("AUTH", default=None)
MONGODB = "mongodb+srv://dilenadaan344:<1GLLNZ0Sy5rFjCsq>@cluster0.8ww20nu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" #config("MONGODB", default=MDB)
OWN = 6679714610 # edit this
GROUP = -1002155139704 # edit this
OWNER_ID = int(config("OWNER_ID", default=OWN))
LOG_GROUP = int(config("LOG_GROUP", default=GROUP))

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
