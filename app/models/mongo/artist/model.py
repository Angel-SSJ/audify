from app.models.mongo.abstractions.base import BaseModelMongo
from app.core.validators.object_id import ObjectID
from app.models.mongo.artist.schemas import (
    Aliases,
    MusicalGenre
)
from app.models.mongo.metrics.schemas import MetricsArtist
from app.models.mongo.media.schemas import ImagesProfileArtist
from app.models.mongo.social.schemas import SocialLinksArtist

class Artist(BaseModelMongo[ObjectID]):
    name: str
    bio: str | None = None
    verified: bool = False
    country_code: str | None = None
    aliases: Aliases | None = None
    genres: list[MusicalGenre] | None = None
    images: ImagesProfileArtist | None = None
    metrics: MetricsArtist | None = None
    social_links: SocialLinksArtist | None = None
