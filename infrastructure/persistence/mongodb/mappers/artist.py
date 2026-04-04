from domain.entities.artist import ArtistEntity
from infrastructure.persistence.mongodb.models.artist.model import Artist
from domain.interfaces.mapper import IMapper
from app.validators.object_id import ObjectID

class ArtistMapper(IMapper[ArtistEntity, Artist]):
    @staticmethod
    def to_domain(persistence_model: Artist) -> ArtistEntity:
        return ArtistEntity(
            id=str(persistence_model.id),
            name=persistence_model.name,
            bio=persistence_model.bio,
            image_url=persistence_model.image_url,
            followers_count=persistence_model.followers_count,
            monthly_listeners=persistence_model.monthly_listeners,
            top_tracks=persistence_model.top_tracks,
            albums=persistence_model.albums,
            related_artists=persistence_model.related_artists,
            country_code=persistence_model.country_code
        )

    @staticmethod
    def to_persistence(domain_entity: ArtistEntity) -> dict:
        data = domain_entity.model_dump(exclude={"id"})
        if domain_entity.id:
            data["_id"] = ObjectID(domain_entity.id)
        return data
