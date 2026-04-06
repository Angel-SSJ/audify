from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.artists import ArtistRepository
from application.services.artists import ArtistsService

async def get_artists_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> ArtistRepository:
    return ArtistRepository(db)

def get_artists_service(
    repo: ArtistRepository = Depends(get_artists_repository),
) -> ArtistsService:
    return ArtistsService(repo)
