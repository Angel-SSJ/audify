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
    def to_persistence(domain_entity: any) -> dict:
        if hasattr(domain_entity, "model_dump"):
            data = domain_entity.model_dump(exclude={"id"}, exclude_none=True)
        elif hasattr(domain_entity, "copy"):
            data = domain_entity.copy()
        else:
            data = dict(domain_entity)

        entity_id = getattr(domain_entity, "id", None)
        if entity_id:
            data["_id"] = ObjectID(entity_id)

        user_id = getattr(domain_entity, "user_id", None)
        if user_id:
            data["user_id"] = ObjectID(user_id)

        track_id = getattr(domain_entity, "track_id", None)
        if track_id:
            data["track_id"] = ObjectID(track_id)

        return data
