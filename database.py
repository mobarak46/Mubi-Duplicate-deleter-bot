from motor.motor_asyncio import AsyncIOMotorClient
import info

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(info.DATABASE_URI)
        self.db = self.client[info.DATABASE_NAME]
        self.col = self.db["seen_files"]
        self.users_col = self.db["users"]

    async def is_duplicate(self, chat_id: int, file_name: str) -> bool:
        """Checks if a file name has already been recorded for this specific channel."""
        doc = await self.col.find_one({"chat_id": chat_id, "file_name": file_name})
        if doc:
            return True
        
        # If it doesn't exist, log it into the database
        await self.col.insert_one({"chat_id": chat_id, "file_name": file_name})
        return False

    async def add_user(self, user_id: int) -> bool:
        """Returns True if the user is new and successfully added, False if they already exist."""
        user = await self.users_col.find_one({"user_id": user_id})
        if not user:
            await self.users_col.insert_one({"user_id": user_id})
            return True
        return False

    async def ping_db(self) -> bool:
        """Pings the database to calculate database latency."""
        try:
            await self.client.admin.command('ping')
            return True
        except Exception:
            return False

db = Database()
