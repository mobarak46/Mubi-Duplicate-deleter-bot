import time
from datetime import datetime
import pytz  # <-- Added for accurate timezone conversion
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import MessageDeleteForbidden

import info
from database import db

bot = Client(
    "file_deleter_bot",
    api_id=info.API_ID,
    api_hash=info.API_HASH,
    bot_token=info.BOT_TOKEN
)

# Global flag initialized at startup to track current live context
START_TIME = time.time()

# Define the IST timezone globally
IST = pytz.timezone('Asia/Kolkata')

# Main Inline Keyboard Setup
def get_main_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_panel"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about_panel")
        ],
        [
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Mobarak46")
        ]
    ])

def get_back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="home_panel")]
    ])

@bot.on_message(filters.command("start") & filters.private)
async def start_cmd(client: Client, message: Message):
    user_id = message.from_user.id
    greeting = info.get_greeting()
    text = info.START_TXT.format(greeting, message.from_user.mention)
    
    # Send the welcome message to the user first
    await message.reply_photo(
        photo=info.START_IMG,
        caption=text,
        reply_markup=get_main_buttons()
    )
    
    # Database check to see if this user is starting the bot for the first time
    is_new = await db.add_user(user_id)
    if is_new:
        log_text = (
            f"<b>#New_User</b>\n\n"
            f"<b>≈ ɪᴅ:-</b> <code>{user_id}</code>\n"
            f"<b>≈ ɴᴀᴍᴇ:-</b> {message.from_user.mention}\n"
            f"<b>≈ ʙᴏᴛ ɴᴀᴍᴇ:-</b> @{client.me.username}"
        )
        try:
            await client.send_message(
                chat_id=info.LOG_CHANNEL,
                text=log_text,
                disable_web_page_preview=True
            )
        except Exception as e:
            print(f"Error sending new user log: {e}")

@bot.on_message(filters.command("ping") & filters.private)
async def ping_cmd(client: Client, message: Message):
    start_ping = time.time()
    
    # Calculate Database Latency
    db_start = time.time()
    await db.ping_db()
    db_latency = (time.time() - db_start) * 1000

    # Calculate Bot Response Latency
    bot_latency = (time.time() - start_ping) * 1000
    
    # Format Timestamp in 12-Hour System passing the IST timezone object
    ist_timestamp = datetime.now(IST).strftime("%Y-%m-%d %I:%M:%S %p")
    
    ping_text = (
        f"🏓 <b>ᴘᴏɴɢ!</b>\n\n"
        f"⚡ <b>ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ:</b> {bot_latency:.2f} ms\n"
        f"🗄️ <b>ᴅᴀᴛᴀʙᴀsᴇ ʟᴀᴛᴇɴᴄʏ:</b> {db_latency:.2f} ms\n"
        f"🤖 <b>ʙᴏᴛ:</b> @{client.me.username}\n"
        f"📡 <b>sᴛᴀᴛᴜs:</b> 🟢 ᴏɴʟɪɴᴇ\n"
        f"⏰ <b>ᴛɪᴍᴇsᴛᴀᴍᴘ:</b> {ist_timestamp}"
    )
    await message.reply_text(ping_text)

@bot.on_callback_query()
async def callback_handler(client: Client, query: CallbackQuery):
    greeting = info.get_greeting()
    
    if query.data == "home_panel":
        await query.message.edit_caption(
            caption=info.START_TXT.format(greeting, query.from_user.mention),
            reply_markup=get_main_buttons()
        )
    elif query.data == "help_panel":
        await query.message.edit_caption(
            caption=info.HELP_TXT.format(query.from_user.mention),
            reply_markup=get_back_button()
        )
    elif query.data == "about_panel":
        await query.message.edit_caption(
            caption=info.ABOUT_TXT,
            reply_markup=get_back_button()
        )

@bot.on_message(filters.channel & (filters.document | filters.video | filters.audio))
async def channel_handler(client: Client, message: Message):
    # Enforce upcoming file rule: ignore old media processed prior to runtime
    if message.date and message.date.timestamp() < START_TIME:
        return

    # Extract file object and safely grab the filename string
    media = message.document or message.video or message.audio
    file_name = getattr(media, "file_name", None)

    if not file_name:
        return

    chat_id = message.chat.id

    # Check and insert verification status through the DB backend
    if await db.is_duplicate(chat_id, file_name):
        try:
            await message.delete()
            
            # Fetch the dynamic current time in IST right as the deletion occurs
            action_time = datetime.now(IST).strftime('%Y-%m-%d %I:%M:%S %p')
            
            # Send an alert to your log channel asynchronously
            await client.send_message(
                chat_id=info.LOG_CHANNEL,
                text=(
                    f"🗑️ <b>--ᴅᴜᴘʟɪᴄᴀᴛᴇ ғɪʟᴇ ᴅᴇʟᴇᴛᴇᴅ--</b>\n\n"
                    f"🌐 <b>ᴄʜᴀɴɴᴇʟ:</b> {message.chat.title} (<code>{chat_id}</code>)\n"
                    f"📄 <b>ғɪʟᴇ ɴᴀᴍᴇ:</b> <code>{file_name}</code>\n"
                    f"⏰ <b>ᴀᴄᴛɪᴏɴ ᴛɪᴍᴇ:</b> {action_time}"
                )
            )
        except MessageDeleteForbidden:
            # Triggered if administrative permissions are missing inside the group channel
            await client.send_message(
                chat_id=info.LOG_CHANNEL,
                text=f"❌ <b>Error:</b> Missing Delete Permission in {message.chat.title}!"
            )
        except Exception as e:
            print(f"Error handling duplicate: {e}")

if __name__ == "__main__":
    print("Mamitha is starting up...")
    bot.run()
    
