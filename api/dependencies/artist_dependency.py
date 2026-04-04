from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.artists import ArtistRepository

async def get_artist_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> ArtistRepository:
    return ArtistRepository(db)
