from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.albums import AlbumsRepository

async def get_album_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> AlbumsRepository:
    return AlbumsRepository(db)
