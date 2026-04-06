from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.playlists import PlaylistRepository
from application.services.playlists import PlaylistsService


async def get_playlists_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> PlaylistRepository:
    return PlaylistRepository(db)

def get_playlists_service(
    repo: PlaylistRepository = Depends(get_playlists_repository),
) -> PlaylistsService:
    return PlaylistsService(repo)
