from datetime import datetime
from pydantic import Field
from app.models.mongo.abstractions.base import BaseModelMongo
from app.core.validators.object_id import ObjectID
from app.models.mongo.enums import MusicalGenre
from app.models.mongo.artist.schemas import ArtistEmbeddedList
from app.models.mongo.media.schemas import VideoAsset

class Track(BaseModelMongo[ObjectID]):
    title: str
    duration_sec: int
    file_url: str
    track_number: int = 0
    genres: list[MusicalGenre] = Field(default_factory=list)
    artists: list[ArtistEmbeddedList] = Field(default_factory=list)
    album_id: ObjectID | None = None
    album_name: str | None = None
    video_assets: VideoAsset | None = None
    cover_image: str
    release_date: datetime | None = None
