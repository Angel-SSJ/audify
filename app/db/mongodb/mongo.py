from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from app.core.config import settings
import os

load_dotenv()

class MongoDB:
    client: AsyncIOMotorClient = None


db = MongoDB()


async def get_mongo_db():
    return db.client[settings.mongo_db]
