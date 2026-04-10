from motor.motor_asyncio import AsyncIOMotorDatabase
from domain.entities.track import TrackEntity
from infrastructure.persistence.mongodb.models.track.model import Track as TrackMongo
from infrastructure.persistence.mongodb.mappers.track import TrackMapper
from infrastructure.persistence.mongodb.repositories.base import BaseRepositoryMongo


class TrackRepository(BaseRepositoryMongo[TrackEntity, TrackMongo]):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(
            db=db,
            collection_name="tracks",
            mapper=TrackMapper(),
            schema_class=TrackMongo,
            entity_name="Track"
        )
