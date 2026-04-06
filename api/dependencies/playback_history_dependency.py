from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.playbacks_history import PlaybackHistoryRepository
from application.services.playback_history import PlaybackHistoryService


async def get_playback_history_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> PlaybackHistoryRepository:
    return PlaybackHistoryRepository(db)

def get_playback_histories_service(
    repo:PlaybackHistoryRepository = Depends(get_playback_history_repository),
) -> PlaybackHistoryService:
    return PlaybackHistoryService(repo)
