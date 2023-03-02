import json
import os
from os import getenv

from dotenv import load_dotenv

load_dotenv()


def get_user_list(config, key):
    with open("{}/Exon/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):"
    LOGGER = True

    API_ID = int(getenv("API_ID", "21029851"))
    API_HASH = getenv("API_HASH", "9217df9a40cf6eaf07f007e96d2cabd7")
    TOKEN = getenv("TOKEN", None)  # ɢᴇᴛ ᴏɴᴇ ғʀᴏᴍ @BotFather [ᴅᴏɴ'ᴛ ᴀᴅᴅ ʜᴇᴀʀ ʙᴏᴛ ᴛᴏᴋᴇɴ ]
    OWNER_ID = int(getenv("OWNER_ID", "6039116006"))  # sᴛᴀʀᴛ @Exon_Robot ᴛʏᴘᴇ /id
    OWNER_USERNAME = getenv("OWNER_USERNAME", "ChinnuXD")  # ʏᴏᴜʀᴇ ᴛɢ ᴜsᴇʀɴᴀᴍᴇ ᴡɪᴛʜᴏᴜᴛ @
    SUPPORT_CHAT = getenv(
        "SUPPORT_CHAT", "our_hub"
    )  # sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ᴡɪᴛʜᴏᴜᴛ @
    EVENT_LOGS = int(
        getenv("EVENT_LOGS", "-1001691352611")
    )  # ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ɪᴅ ᴡɪᴛɢ (-)
    MONGO_DB_URI = getenv(
        "MONGO_DB_URI", "mongodb+srv://chinuxd:chinuxd@cluster0.1jucob6.mongodb.net/?retryWrites=true&w=majority"
    )  # ʀᴇǫᴜɪʀᴇᴅ ғᴏʀ ᴅᴀᴛᴀʙᴀsᴇ ᴄᴏɴɴᴇᴄᴛɪᴏɴs (ᴍᴏɴɢᴏ - https://cloud.mongodb.com/)
    DB_NAME = getenv("DB_NAME", "EXON_2")  # ᴅʙ  ɴᴀᴍᴇ
    DATABASE_URL = getenv(
        "DATABASE_URL", ""
    )  # ʀᴇǫᴜɪʀᴇᴅ ғᴏʀ ᴅᴀᴛᴀʙᴀsᴇ ᴄᴏɴɴᴇᴄᴛɪᴏɴs (sǫʟ :- elephantsql.com).",

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

    LOAD = []
    NO_LOAD = []
    BL_CHATS = []
    DRAGONS = get_user_list("elevated_users.json", "sudos")  # ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DEV_USERS = get_user_list("elevated_users.json", "devs")  # ᴅᴏɴ'ᴛ ᴇᴅɪᴛ


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
