from pydantic import BaseModel, Field
from datetime import datetime
from domain.abstractions.enums import MusicalGenre, ReleaseType
from domain.object_values.track_embeddings import TrackEmbeddedAlbum

class CreateAlbumDTO(BaseModel):
    title: str
    artist_id: str
    artist_name: str
    release_type: ReleaseType
    release_date: datetime
    genres: list[MusicalGenre] = Field(default_factory=list)
    total_tracks: int = 0
    cover_url: str
    tracks: list[TrackEmbeddedAlbum] = Field(default_factory=list)

class UpdateAlbumDTO(BaseModel):
    title: str | None = None
    artist_id: str | None = None
    artist_name: str | None = None
    release_type: ReleaseType | None = None
    release_date: datetime | None = None
    genres: list[MusicalGenre] | None = None
    total_tracks: int | None = None
    cover_url: str | None = None
    tracks: list[TrackEmbeddedAlbum] | None = None


class AlbumResponse(BaseModel):
    id: str
    title: str
    artist_id: str
    artist_name: str
    release_type: str
    release_date: datetime
    genres: list[str] = []
    total_tracks: int = 0
    cover_url: str
    tracks: list[TrackEmbeddedAlbum] = []

    class Config:
        from_attributes = True
