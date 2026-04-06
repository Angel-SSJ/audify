from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.tracks import TrackRepository
from application.services.tracks import TracksService

async def get_tracks_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> TrackRepository:
    return TrackRepository(db)

def get_tracks_service(
    repo: TrackRepository = Depends(get_tracks_repository),
) -> TracksService:
    return TracksService(repo)
