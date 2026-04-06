from pydantic import BaseModel, Field
from domain.abstractions.enums import MusicalGenre

class CreateArtistDTO(BaseModel):
    name: str
    biography: str
    image_url: str
    genres: list[MusicalGenre] = Field(default_factory=list)
    country: str


class UpdateArtistDTO(BaseModel):
    name: str | None = None
    biography: str | None = None
    image_url: str | None = None
    genres: list[MusicalGenre] | None = None
    country: str | None = None


class ArtistResponse(BaseModel):
    id: str
    name: str
    bio: str | None = None
    verified: bool
    country_code: str | None = None
    aliases: list[str] = []
    genres: list[str] = []
    images: dict | None = None
    metrics: dict | None = None
    social_links: dict | None = None

    class Config:
        from_attributes = True
