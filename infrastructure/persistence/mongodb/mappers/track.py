from domain.entities.track import TrackEntity
from infrastructure.persistence.mongodb.models.track.model import Track
from domain.interfaces.mapper import IMapper
from api.helpers.object_id import ObjectID
from domain.object_values.artist_embedded_track import ArtistEmbeddedTrack
from infrastructure.persistence.mongodb.models.enums import ArtistRole

class TrackMapper(IMapper[TrackEntity, Track]):
    @staticmethod
    def to_domain(persistence_model: Track) -> TrackEntity:
        return TrackEntity(
            id=str(persistence_model.id),
            title=persistence_model.title,
            duration_sec=persistence_model.duration_sec,
            file_url=persistence_model.file_url,
            track_number=persistence_model.track_number,
            genres=[genre.value for genre in persistence_model.genres] if persistence_model.genres else [],
            artists= [
                ArtistEmbeddedTrack(
                    artist_id=str(artist.artist_id),
                    name=artist.name,
                    role=artist.role.value if isinstance(artist.role, ArtistRole) else str(artist.role)
                ) for artist in persistence_model.artists] if persistence_model.artists else [],
            album_id=str(persistence_model.album_id),
            album_name=persistence_model.album_name,
            video_assets=persistence_model.video_assets.model_dump() if persistence_model.video_assets else None,
            cover_image=persistence_model.cover_image,
            release_date=persistence_model.release_date
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

        album_id = getattr(domain_entity, "album_id", None)
        if album_id:
            data["album_id"] = ObjectID(album_id)

        if hasattr(domain_entity, "artists") and domain_entity.artists:
            data["artists"] = []
            for artist in domain_entity.artists:
                artist_data = artist.model_dump() if hasattr(artist, "model_dump") else artist
                if isinstance(artist_data, dict):
                    artist_id = artist_data.get("artist_id")
                    if artist_id:
                        artist_data["artist_id"] = ObjectID(artist_id)
                data["artists"].append(artist_data)

        return data
