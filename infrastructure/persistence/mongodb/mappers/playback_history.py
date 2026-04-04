from domain.entities.playback_history import PlaybackHistoryEntity
from infrastructure.persistence.mongodb.models.playback_history.model import PlaybackHistory
from domain.interfaces.mapper import IMapper
from app.validators.object_id import ObjectID

class PlaybackHistoryMapper(IMapper[PlaybackHistoryEntity, PlaybackHistory]):
    @staticmethod
    def to_domain(persistence_model: PlaybackHistory) -> PlaybackHistoryEntity:
        return PlaybackHistoryEntity(
            id=str(persistence_model.id),
            user_id=persistence_model.user_id,
            track_id=persistence_model.track_id,
            played_at=persistence_model.played_at,
            progress_ms=persistence_model.progress_ms,
            track_duration_ms=persistence_model.track_duration_ms,
            percent_played=persistence_model.percent_played,
            interactions=persistence_model.interactions,
            context=persistence_model.context,
            device=persistence_model.device,
            country_code=persistence_model.country_code
        )

    @staticmethod
    def to_persistence(domain_entity: PlaybackHistoryEntity) -> dict:
        data = domain_entity.model_dump(exclude={"id"})
        if domain_entity.id:
            data["_id"] = ObjectID(domain_entity.id)
        return data
