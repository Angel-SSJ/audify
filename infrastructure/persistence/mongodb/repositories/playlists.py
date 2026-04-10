from motor.motor_asyncio import AsyncIOMotorDatabase
from domain.entities.playlist import PlaylistEntity
from infrastructure.persistence.mongodb.models.playlist.model import Playlist
from infrastructure.persistence.mongodb.mappers.playlist import PlaylistMapper
from infrastructure.persistence.mongodb.repositories.base import BaseRepositoryMongo


class PlaylistRepository(BaseRepositoryMongo[PlaylistEntity, Playlist]):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(
            db=db,
            collection_name="playlists",
            mapper=PlaylistMapper(),
            schema_class=Playlist,
            entity_name="Playlist"
        )

