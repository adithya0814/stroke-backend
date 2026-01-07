import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_DETAILS = os.environ.get("MONGO_DETAILS", "mongodb://localhost")
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.stroke_recovery
user_collection = database.get_collection("users")

async def delete_user():
    email = "adithyaadhi513@gmail.com"
    result = await user_collection.delete_one({"email": email})
    if result.deleted_count > 0:
        print(f"Successfully deleted user with email: {email}")
    else:
        print(f"No user found with email: {email}")

if __name__ == "__main__":
    asyncio.run(delete_user())
