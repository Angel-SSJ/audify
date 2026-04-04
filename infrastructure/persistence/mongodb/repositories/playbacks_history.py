from motor.motor_asyncio import AsyncIOMotorDatabase
from domain.entities.playback_history import PlaybackHistoryEntity
from infrastructure.persistence.mongodb.models.playback_history.model import PlaybackHistory
from infrastructure.persistence.mongodb.mappers.playback_history import PlaybackHistoryMapper
from infrastructure.persistence.mongodb.repositories.base import BaseRepositoryMongo


class PlaybackHistoryRepository(BaseRepositoryMongo[PlaybackHistoryEntity, PlaybackHistory]):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(
            db=db,
            collection_name="playback_history",
            mapper=PlaybackHistoryMapper(),
            schema_class=PlaybackHistory,
        )

