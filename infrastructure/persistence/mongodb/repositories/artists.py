from motor.motor_asyncio import AsyncIOMotorDatabase
from domain.entities.artist import ArtistEntity
from infrastructure.persistence.mongodb.models.artist.model import Artist
from infrastructure.persistence.mongodb.mappers.artist import ArtistMapper
from infrastructure.persistence.mongodb.repositories.base import BaseRepositoryMongo


class ArtistRepository(BaseRepositoryMongo[ArtistEntity, Artist]):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(
            db=db,
            collection_name="artists",
            mapper=ArtistMapper(),
            schema_class=Artist,
            entity_name="Artist"
        )

