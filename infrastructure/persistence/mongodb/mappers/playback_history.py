from domain.entities.playback_history import PlaybackHistoryEntity
from infrastructure.persistence.mongodb.models.playback_history.model import PlaybackHistory
from domain.interfaces.mapper import IMapper
from api.helpers.object_id import ObjectID

class PlaybackHistoryMapper(IMapper[PlaybackHistoryEntity, PlaybackHistory]):
    @staticmethod
    def to_domain(persistence_model: PlaybackHistory) -> PlaybackHistoryEntity:
        return PlaybackHistoryEntity(
            id=str(persistence_model.id),
            user_id=str(persistence_model.user_id),
            track_id=str(persistence_model.track_id),
            played_at=persistence_model.played_at,
            progress_ms=persistence_model.progress_ms,
            track_duration_ms=persistence_model.track_duration_ms,
            percent_played=persistence_model.percent_played,
            interactions=persistence_model.interactions.model_dump() if persistence_model.interactions else None,
            context=persistence_model.context.model_dump() if persistence_model.context else None,
            device=persistence_model.device.model_dump() if persistence_model.device else None,
            country_code=persistence_model.country_code
        )

    @staticmethod
    def to_persistence(domain_entity: PlaybackHistoryEntity) -> dict:
        data = domain_entity.model_dump(exclude={"id"})
        if domain_entity.id:
            data["_id"] = ObjectID(domain_entity.id)

        if domain_entity.user_id:
            data["user_id"] = ObjectID(domain_entity.user_id)
        if domain_entity.track_id:
            data["track_id"] = ObjectID(domain_entity.track_id)

        return data
