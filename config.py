import os
import logging
from logging.handlers import RotatingFileHandler
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")
#Your channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#start message
START_MSG = os.environ.get("START_MESSAGE", "Hai {firstname}\n\nSaya dapat menyimpan file pribadi di Saluran Tertentu dan pengguna lain dapat mengaksesnya dari tautan khusus..")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Daftar Admin Anda tidak berisi bilangan bulat yang valid.")

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
