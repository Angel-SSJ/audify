from datetime import datetime
from pydantic import Field
from app.models.mongo.abstractions.base import BaseModelMongo
from app.models.mongo.enums import ReleaseType, MusicalGenre
from app.core.validators.object_id import ObjectID
from app.models.mongo.track.schemas import TrackEmbeddedAlbum

class Album(BaseModelMongo):
    title: str
    artist_id: ObjectID
    artist_name: str
    release_type: ReleaseType
    release_date: datetime
    genres: list[MusicalGenre] = Field(default_factory=list)
    total_tracks: int = 0
    cover_url: str
    tracks: list[TrackEmbeddedAlbum] = Field(default_factory=list)
