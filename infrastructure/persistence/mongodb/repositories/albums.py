from motor.motor_asyncio import AsyncIOMotorDatabase
from domain.entities.album import AlbumEntity
from infrastructure.persistence.mongodb.models.album.model import Album
from infrastructure.persistence.mongodb.mappers.album import AlbumMapper
from infrastructure.persistence.mongodb.repositories.base import BaseRepositoryMongo


class AlbumsRepository(BaseRepositoryMongo[AlbumEntity, Album]):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(
            db=db,
            collection_name="albums",
            mapper=AlbumMapper(),
            schema_class=Album,
            entity_name="Album"
        )

