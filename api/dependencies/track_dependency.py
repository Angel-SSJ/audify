from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.tracks import TrackRepository

async def get_track_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> TrackRepository:
    return TrackRepository(db)
