import os
import time

# API Configuration
API_ID = int(os.environ.get("API_ID", ""))  # Replace with your actual Values
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN_ID = int(os.environ.get("ADMIN_ID", ""))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

# Database Configuration
DATABASE_NAME = os.environ.get("DATABASE_NAME", "MUBIXDELETERBOT")
DATABASE_URI = os.environ.get("DATABASE_URI", "")

# Assets
START_IMG = os.environ.get("START_IMG", "")

# Bot Startup Greeting Logic (IST UTC+5:30)
def get_greeting():
    current_time = time.gmtime(time.time() + 19800)
    if current_time.tm_hour == 5:
        return "🌅 Good Morning Boss! 📊\n\n"
    return ""

# UI Text Variables
START_TXT = """{}ʜᴇʟʟᴏ {}
Welcome to Duplicate File Deleter Bot! I monitor your channel in real-time and automatically eliminate identical upcoming duplicate files."""

HELP_TXT = """ʜᴇʟʟᴏ {}
ʜᴇʀᴇ ɪs ᴀʟʟ ᴍʏ ᴜsᴇғᴜʟʟ ғᴇᴀᴛᴜʀᴇs.

• Add me to your channel as an Administrator with delete messages permission.
• I will automatically delete any incoming file that matches a file name already posted since my activation.
• /ping - Check real-time response and database latency."""

ABOUT_TXT = """<b>❍ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/Mubi_Bot">Ѕᴀᴍᴀɴᴛʜᴀ</a>
❍ ᴅᴇᴠᴇʟᴏᴩᴇʀ : <a href="https://t.me/Mobarak46">Mᴜʙɪ</a>
❍ ɢɪᴛʜᴜʙ : <a href="https://github.com/Mobarak46">Mᴜʙɪ</a>
❍ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>
❍ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
❍ ʜᴏꜱᴛᴇᴅ ᴏɴ : <a href="https://t.me/MUBIBOTz">ᴠᴘs</a></b>"""

SOURCE_TXT = "https://github.com/Mobarak46"
