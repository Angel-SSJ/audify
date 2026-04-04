from domain.entities.playlist import PlaylistEntity
from infrastructure.persistence.mongodb.models.playlist.model import Playlist
from domain.interfaces.mapper import IMapper
from app.validators.object_id import ObjectID
from infrastructure.persistence.mongodb.models.track.schemas import TrackEmbeddedPlaylist

class PlaylistMapper(IMapper[PlaylistEntity, Playlist]):
    @staticmethod
    def to_domain(persistence_model: Playlist) -> PlaylistEntity:
        return PlaylistEntity(
            id=str(persistence_model.id),
            name=persistence_model.name,
            description=persistence_model.description,
            owner_id=persistence_model.owner_id,
            is_public=persistence_model.is_public,
            followers_count=persistence_model.followers_count,
            cover_image=persistence_model.cover_image,
            tracks=[TrackEmbeddedPlaylist(
                track_id=str(track.track_id),
                title=track.title,
                duration_sec=track.duration_sec,
                cover_image=track.cover_image,
                added_at=track.added_at,
                artist_name=track.artist_name,
            ) for track in persistence_model.tracks],
            total_duration_sec=persistence_model.total_duration_sec,
            total_tracks=persistence_model.total_tracks
        )

    @staticmethod
    def to_persistence(domain_entity: PlaylistEntity) -> dict:
        data = domain_entity.model_dump(exclude={"id"})
        if domain_entity.id:
            data["_id"] = ObjectID(domain_entity.id)
        return data
