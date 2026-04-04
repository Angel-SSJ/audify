from infrastructure.persistence.mongodb.models.abstractions.base import BaseModelMongo
from app.validators.object_id import ObjectID
from infrastructure.persistence.mongodb.models.artist.schemas import (
    Aliases,
    MusicalGenre
)
from infrastructure.persistence.mongodb.models.metrics.schemas import MetricsArtist
from infrastructure.persistence.mongodb.models.media.schemas import ImagesProfileArtist
from infrastructure.persistence.mongodb.models.social.schemas import SocialLinksArtist
from pydantic import Field

class Artist(BaseModelMongo[ObjectID]):
    name: str
    bio: str | None = None
    verified: bool = False
    country_code: str | None = None
    aliases: list[str] = Field(default_factory=list)
    genres: list[MusicalGenre] | None = None
    images: ImagesProfileArtist | None = None
    metrics: MetricsArtist | None = None
    social_links: SocialLinksArtist | None = None
