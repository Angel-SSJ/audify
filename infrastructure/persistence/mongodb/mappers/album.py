from domain.entities.album import AlbumEntity
from infrastructure.persistence.mongodb.models.album.model import Album
from domain.interfaces.mapper import IMapper
from app.validators.object_id import ObjectID


class AlbumMapper(IMapper[AlbumEntity, Album]):
    @staticmethod
    def to_domain(persistence_model: Album) -> AlbumEntity:
        return AlbumEntity(
            id=str(persistence_model.id),
            title=persistence_model.title,
            artist_id=persistence_model.artist_id,
            artist_name=persistence_model.artist_name,
            release_type=persistence_model.release_type,
            release_date=persistence_model.release_date,
            genres=persistence_model.genres,
            total_tracks=persistence_model.total_tracks,
            cover_url=persistence_model.cover_url,
            tracks=persistence_model.tracks,
        )

    @staticmethod
    def to_persistence(domain_entity: AlbumEntity) -> dict:
        data = domain_entity.model_dump(exclude={"id"})
        if domain_entity.id:
            data["_id"] = ObjectID(domain_entity.id)
        return data
