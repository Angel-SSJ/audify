from domain.abstractions.base import BaseEntity
from domain.object_values.track_embeddings import TrackEmbeddedAlbum
from app.validators.object_id import ObjectID
from pydantic import Field
from datetime import datetime
from domain.abstractions.enums import MusicalGenre, ReleaseType

class AlbumEntity(BaseEntity):
    title: str
    artist_id: ObjectID
    artist_name: str
    release_type: ReleaseType
    release_date: datetime
    genres: list[MusicalGenre] = Field(default_factory=list)
    total_tracks: int = 0
    cover_url: str
    tracks: list[TrackEmbeddedAlbum] = Field(default_factory=list)
