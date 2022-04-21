import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ᴜғᴏ ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/11fb9881a34e73137703b.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/11fb9881a34e73137703b.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/11fb9881a34e73137703b.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/11fb9881a34e73137703b.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "EEBB_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "YA_FE")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CHTLHB")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ALRAGIBOT")
OWNER_NAME = getenv("OWNER_NAME", "PFPFF") 
DEV_NAME = getenv("DEV_NAME", "PFPFF")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
