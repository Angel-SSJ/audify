from datetime import datetime
from pydantic import Field
from infrastructure.persistence.mongodb.models.abstractions.base import BaseModelMongo
from api.helpers.object_id import ObjectID
from infrastructure.persistence.mongodb.models.enums import MusicalGenre
from infrastructure.persistence.mongodb.models.media.schemas import VideoAsset
from infrastructure.persistence.mongodb.models.track.schemas import ArtistEmbeddedTrack

class Track(BaseModelMongo[ObjectID]):
    title: str
    duration_sec: int
    file_url: str
    track_number: int = 0
    genres: list[MusicalGenre] = Field(default_factory=list)
    artists:list[ArtistEmbeddedTrack] = Field(default_factory=list)
    album_id: ObjectID | None = None
    album_name: str | None = None
    video_assets: VideoAsset | None = None
    cover_image: str
    release_date: datetime | None = None
