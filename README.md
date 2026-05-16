# Ꮇᴀᴍɪᴛʜᴀ | Telegram Duplicate File Deleter Bot 🗑️
A lightweight, real-time Telegram channel monitoring bot built using the **Pyrogram** framework. It automatically tracks incoming media uploads (documents, videos, and audio files) and instantly eliminates duplicate posts based on filename verification backed by a **MongoDB** cluster.
---
## 🚀 Features
* 🔁 **Real-Time Deletion:** Scans and eliminates duplicate media files instantly upon arrival.
* ⏱️ **Timezone Synchronized:** Precise tracking with localized **India Standard Time (IST)** action logs.
* 🛡️ **Fail-Safe Startup:** Incorporates an upfront protection runtime check that ignores historical content posted before the bot went online.
* 📊 **Live Diagnostics:** Integrated `/ping` utility command checking structural bot response times and database backend latency metrics.
* 📝 **Detailed Logging:** Automatically dispatches structured administrative execution telemetry to a dedicated log channel.
---
## 🛠️ Environment Variables & Configuration
To run this bot, you need to configure the following environment variables. You can assign these via your host environment setup or within an `info.py` module file:

| Variable Name | Description |
| :--- | :--- |
| `API_ID` | Your Telegram Application API ID. |
| `API_HASH` | Your Telegram Application API Hash signature. |
| `BOT_TOKEN` | Telegram Bot Token received from [@BotFather](https://t.me/BotFather). |
| `ADMIN_ID` | Unique Telegram User ID of the primary owner. |
| `LOG_CHANNEL` | Target Telegram Channel ID (`-100...`) for logging system actions. |
| `DATABASE_NAME` | Name identifier assigned inside your MongoDB database cluster. |
| `DATABASE_URI` | Full connection URI access string for MongoDB database instance. |
| `START_IMG` | Public URL reference for the image utilized during `/start`. |

---
## 📦 Deployment Setup
### 1. Prerequisites
Ensure you have Python 3.9+ installed on your deployment server environment.
### 2. Install Dependencies
Install all required package frameworks and timezone data modules:


<b>⚙️ Administrative Setup Notes

To ensure the bot operates correctly in your channels, apply the following settings:

• Channel Access: Add Mamitha into your target tracking channels as an Administrator.
• Permissions Required: Ensure the bot is granted "Delete Messages" permissions.
• Fail-safe: Without this explicit administrative capability, the engine will fail to execute actions cleanly and will drop an operational alert warning directly into your configured log channel feed.

⚖️ License & Credits

• Developer: <a href="https://t.me/Mobarak46">Mubi</a>
• Framework: Powered by <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>
• Database: Powered by <a href="https://www.mongodb.com/">MongoDB</a>

Distributed under the MIT License. See the LICENSE configuration mappings for more details.</b>
