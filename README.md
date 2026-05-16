<p align="center">
  <img src="https://i.ibb.co/1J9G7szZ/x.jpg" alt="Mamitha Bot Banner" width="100%">
</p>

<b># Ꮇᴀᴍɪᴛʜᴀ | Telegram Duplicate File Deleter Bot 🗑️</b>

<b>A lightweight, real-time Telegram channel monitoring bot built using the Pyrogram framework. It automatically tracks incoming media uploads (documents, videos, and audio files) and instantly eliminates duplicate posts based on filename verification backed by a MongoDB cluster.</b>

---

## 🚀 Features

<b>🔁 Real-Time Deletion:</b> Scans and eliminates duplicate media files instantly upon arrival.

<b>⏱️ Timezone Synchronized:</b> Precise tracking with localized <b>India Standard Time (IST)</b> action logs.

<b>🛡️ Fail-Safe Startup:</b> Incorporates an upfront protection runtime check that ignores historical content posted before the bot went online.

<b>📊 Live Diagnostics:</b> Integrated <code>/ping</code> utility command checking structural bot response times and database backend latency metrics.

<b>📝 Detailed Logging:</b> Automatically dispatches structured administrative execution telemetry to a dedicated log channel.

---

## 🛠️ Environment Variables & Configuration

To run this bot, you need to configure the following environment variables. You can assign these via your host environment setup or within an <code>info.py</code> module file:

| Variable Name | Description |
| :--- | :--- |
| <code>API_ID</code> | Your Telegram Application API ID. |
| <code>API_HASH</code> | Your Telegram Application API Hash signature. |
| <code>BOT_TOKEN</code> | Telegram Bot Token received from <a href="https://t.me/BotFather">@BotFather</a>. |
| <code>ADMIN_ID</code> | Unique Telegram User ID of the primary owner. |
| <code>LOG_CHANNEL</code> | Target Telegram Channel ID (<code>-100...</code>) for logging system actions. |
| <code>DATABASE_NAME</code> | Name identifier assigned inside your MongoDB database cluster. |
| <code>DATABASE_URI</code> | Full connection URI access string for MongoDB database instance. |
| <code>START_IMG</code> | Public URL reference for the image utilized during <code>/start</code>. |

---

## 📦 Deployment Setup

### 1. Prerequisites

Ensure you have Python 3.9+ installed on your deployment server environment.

### 2. Install Dependencies

Install all required package frameworks and timezone data modules:
pip install pyrogram tgcrypto pytz pymongo motor

<b>⚙️ Administrative Setup Notes</b>

To ensure the bot operates correctly in your channels, apply the following settings:

<b>• Channel Access:</b> Add Mamitha into your target tracking channels as an Administrator.

<b>• Permissions Required:</b> Ensure the bot is granted "Delete Messages" permissions.

<b>• Fail-safe:</b> Without this explicit administrative capability, the engine will fail to execute actions cleanly and will drop an operational alert warning directly into your configured log channel feed.

<b>⚖️ License & Credits</b>

<b>• Developer:</b> <a href="https://t.me/Mobarak46">Mubi</a>

<b>• Framework:</b> Powered by <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>

<b>• Database:</b> Powered by <a href="https://www.mongodb.com/">MongoDB</a>

<b>Distributed under the MIT License. See the LICENSE configuration mappings for more details.</b>
