from pydantic import BaseModel, Field
from domain.abstractions.enums import MusicalGenre
from domain.object_values.metrics_artist import MetricsArtist
from domain.object_values.social_links_artist import SocialLinksArtist
from domain.object_values.images_profile_artists import ImagesProfileArtist

class CreateArtistDTO(BaseModel):
    name: str
    bio: str
    image_url: str
    genres: list[MusicalGenre] = Field(default_factory=list)
    country: str
    verified: bool = False
    aliases: list[str] = Field(default_factory=list)
    images: ImagesProfileArtist | None = None
    metrics: MetricsArtist | None = None
    social_links: SocialLinksArtist | None = None


class UpdateArtistDTO(BaseModel):
    name: str | None = None
    bio: str | None = None
    verified: bool | None = None
    country_code: str | None = None
    aliases: list[str] | None = None
    genres: list[MusicalGenre] | None = None
    images: ImagesProfileArtist | None = None
    metrics: MetricsArtist | None = None
    social_links: SocialLinksArtist | None = None




class ArtistResponse(BaseModel):
    id: str
    name: str
    bio: str | None = None
    verified: bool
    country_code: str | None = None
    aliases: list[str] = []
    genres: list[str] = []
    images: ImagesProfileArtist | None = None
    metrics: MetricsArtist | None = None
    social_links: SocialLinksArtist | None = None

    class Config:
        from_attributes = True
