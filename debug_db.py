import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.environ.get("MONGO_DETAILS", "mongodb://localhost")
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.stroke_recovery
user_collection = database.get_collection("users")

async def check_user():
    print("Listing all users in DB:")
    async for user in user_collection.find():
        print(f"--- User Found ---")
        print(f"Username: '{user.get('username')}'")
        print(f"Email:    '{user.get('email')}'")
        print(f"Password: '{user.get('password')}'")

if __name__ == "__main__":
    asyncio.run(check_user())
