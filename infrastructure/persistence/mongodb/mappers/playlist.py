from domain.entities.playlist import PlaylistEntity
from infrastructure.persistence.mongodb.models.playlist.model import Playlist
from domain.interfaces.mapper import IMapper
from api.helpers.object_id import ObjectID
from infrastructure.persistence.mongodb.models.track.schemas import TrackEmbeddedPlaylist

class PlaylistMapper(IMapper[PlaylistEntity, Playlist]):
    @staticmethod
    def to_domain(persistence_model: Playlist) -> PlaylistEntity:
        return PlaylistEntity(
            id=str(persistence_model.id),
            name=persistence_model.name or '',
            description=persistence_model.description or '',
            owner_id=str(persistence_model.owner_id),
            is_public=persistence_model.is_public if persistence_model.is_public is not None else True,
            followers_count=persistence_model.followers_count or 0,
            cover_image=persistence_model.cover_image or '',
            tracks=[
                {
                    **track.model_dump(),
                    "track_id": str(track.track_id)
                } for track in persistence_model.tracks
            ] if persistence_model.tracks else [],
            total_duration_sec=persistence_model.total_duration_sec or 0,
            total_tracks=persistence_model.total_tracks or 0
        )

    @staticmethod
    def to_persistence(domain_entity: any) -> dict:
        if hasattr(domain_entity, "model_dump"):
            data = domain_entity.model_dump(exclude={"id"},exclude_unset=True)
        elif hasattr(domain_entity, "copy"):
            data = domain_entity.copy()
        else:
            data = dict(domain_entity)

        entity_id = getattr(domain_entity, "id", None)
        if entity_id:
            data["_id"] = ObjectID(entity_id)

        owner_id = getattr(domain_entity, "owner_id", None)
        if owner_id:
            data["owner_id"] = ObjectID(owner_id)

        if hasattr(domain_entity, "tracks") and domain_entity.tracks:
            data["tracks"] = []
            for track in domain_entity.tracks:
                track_data = track.model_dump() if hasattr(track, "model_dump") else track
                if isinstance(track_data, dict):
                    track_id = track_data.get("track_id")
                    if track_id:
                        track_data["track_id"] = ObjectID(track_id)
                data["tracks"].append(track_data)

        return data
