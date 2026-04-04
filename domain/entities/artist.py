from domain.abstractions.base import BaseEntity
from domain.abstractions.enums import MusicalGenre
from domain.object_values.metrics_artist import MetricsArtist
from domain.object_values.social_links_artist import SocialLinksArtist
from domain.object_values.images_profile_artists import ImagesProfileArtist
from pydantic import Field

class ArtistEntity(BaseEntity):
    name: str
    bio: str | None = None
    verified: bool = False
    country_code: str | None = None
    aliases: list[str] = Field(default_factory=list)
    genres: list[MusicalGenre] | None = None
    images: ImagesProfileArtist | None = None
    metrics: MetricsArtist | None = None
    social_links: SocialLinksArtist | None = None
