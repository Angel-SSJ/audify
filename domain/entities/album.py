from domain.object_values.track_embeddings import TrackEmbeddedAlbum
from pydantic import Field
from datetime import datetime
from domain.abstractions.enums import MusicalGenre, ReleaseType
from domain.abstractions.base import BaseEntity

class AlbumEntity(BaseEntity):
    title: str
    artist_id: str
    artist_name: str
    release_type: ReleaseType
    release_date: datetime
    genres: list[MusicalGenre] = Field(default_factory=list)
    total_tracks: int = 0
    cover_url: str
    tracks: list[TrackEmbeddedAlbum] = Field(default_factory=list)
