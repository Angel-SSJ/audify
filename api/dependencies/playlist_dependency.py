from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.playlists import PlaylistRepository

async def get_playlist_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> PlaylistRepository:
    return PlaylistRepository(db)
