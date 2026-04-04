from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.users import UserRepository


async def get_user_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> UserRepository:
    return UserRepository(db)
