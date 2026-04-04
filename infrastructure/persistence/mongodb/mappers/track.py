from domain.entities.track import TrackEntity
from infrastructure.persistence.mongodb.models.track.model import Track
from domain.interfaces.mapper import IMapper
from app.validators.object_id import ObjectID
from domain.object_values.track_embeddings import TrackEmbeddedPlaylist


class TrackMapper(IMapper[TrackEntity, Track]):
    @staticmethod
    def to_domain(persistence_model: Track) -> TrackEntity:
        return TrackEntity(
            id=str(persistence_model.id),
            title=persistence_model.title,
            duration_sec=persistence_model.duration_sec,
            file_url=persistence_model.file_url,
            track_number=persistence_model.track_number,
            genres=persistence_model.genres,
            artists=persistence_model.artists,
            album_id=persistence_model.album_id,
            album_name=persistence_model.album_name,
            video_assets=persistence_model.video_assets,
            cover_image=persistence_model.cover_image,
            release_date=persistence_model.release_date
        )

    @staticmethod
    def to_persistence(domain_entity: TrackEntity) -> dict:
        data = domain_entity.model_dump(exclude={"id"})
        if domain_entity.id:
            data["_id"] = ObjectID(domain_entity.id)
        return data
