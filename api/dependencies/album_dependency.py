from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.albums import AlbumsRepository
from application.services.albums import AlbumsService

async def get_albums_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> AlbumsRepository:
    return AlbumsRepository(db)

def get_albums_service(
    repo: AlbumsRepository = Depends(get_albums_repository),
) -> AlbumsService:
    return AlbumsService(repo)
