import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1916166816:AAFw6-yxZOFLkR-FRSp4rsgc_jToRifUiUM")

    API_ID = int(os.environ.get("API_ID", 4674611))

    API_HASH = os.environ.get("API_HASH", "65094863055d68954505ce9d6eef6aa1")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1756775763").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @VidProBot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "")

    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001892745853))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "1756775763"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "UploadLinkToFileBot")

    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))

    PRO_USERS.append(OWNER_ID)