from domain.entities.album import AlbumEntity
from infrastructure.persistence.mongodb.models.album.model import Album
from domain.interfaces.mapper import IMapper
from api.helpers.object_id import ObjectID


class AlbumMapper(IMapper[AlbumEntity, Album]):
    @staticmethod
    def to_domain(persistence_model: Album) -> AlbumEntity:
        return AlbumEntity(
            id=str(persistence_model.id),
            title=persistence_model.title,
            artist_id=str(persistence_model.artist_id),
            artist_name=persistence_model.artist_name,
            release_type=persistence_model.release_type.value if persistence_model.release_type else None,
            release_date=persistence_model.release_date,
            genres=[genre.value for genre in persistence_model.genres] if persistence_model.genres else [],
            total_tracks=persistence_model.total_tracks,
            cover_url=persistence_model.cover_url,
            tracks=[
                {
                    **track.model_dump(),
                    "track_id": str(track.track_id)
                } for track in persistence_model.tracks
            ] if persistence_model.tracks else [],
        )

    @staticmethod
    def to_persistence(domain_entity: AlbumEntity) -> dict:
        data = domain_entity.model_dump(exclude={"id"})
        if domain_entity.id:
            data["_id"] = ObjectID(domain_entity.id)
            
        if domain_entity.artist_id:
            data["artist_id"] = ObjectID(domain_entity.artist_id)
            
        return data
