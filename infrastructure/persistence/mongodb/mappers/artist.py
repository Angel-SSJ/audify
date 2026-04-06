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
            verified=persistence_model.verified,
            country_code=persistence_model.country_code,
            aliases=persistence_model.aliases,
            genres=[genre.value for genre in persistence_model.genres] if persistence_model.genres else [],
            images=persistence_model.images.model_dump() if persistence_model.images else None,
            metrics=persistence_model.metrics.model_dump() if persistence_model.metrics else None,
            social_links=persistence_model.social_links.model_dump() if persistence_model.social_links else None,
        )

    @staticmethod
    def to_persistence(domain_entity: ArtistEntity) -> dict:
        data = domain_entity.model_dump(exclude={"id"})
        if domain_entity.id:
            data["_id"] = ObjectID(domain_entity.id)
        return data
