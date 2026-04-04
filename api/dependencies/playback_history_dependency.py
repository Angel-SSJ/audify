from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.playbacks_history import PlaybackHistoryRepository

async def get_playback_history_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> PlaybackHistoryRepository:
    return PlaybackHistoryRepository(db)
