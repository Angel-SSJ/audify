from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.config import settings


class MongoDB:
    client: AsyncIOMotorClient = None


db = MongoDB()


async def get_mongo_db() -> AsyncIOMotorDatabase:
    return db.client[settings.mongo_db]

