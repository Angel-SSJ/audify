from datetime import datetime
from pydantic import Field
from infrastructure.persistence.mongodb.models.abstractions.base import BaseModelMongo
from infrastructure.persistence.mongodb.models.enums import ReleaseType, MusicalGenre
from app.validators.object_id import ObjectID
from infrastructure.persistence.mongodb.models.track.schemas import TrackEmbeddedAlbum

class Album(BaseModelMongo[ObjectID]):
    title: str
    artist_id: ObjectID
    artist_name: str
    release_type: ReleaseType
    release_date: datetime
    genres: list[MusicalGenre] = Field(default_factory=list)
    total_tracks: int = 0
    cover_url: str
    tracks: list[TrackEmbeddedAlbum] = Field(default_factory=list)
