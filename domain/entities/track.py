from domain.abstractions.base import BaseEntity
from pydantic import Field
from app.validators.object_id import ObjectID
from datetime import datetime
from domain.object_values.artist_embeddings import ArtistEmbeddedList
from domain.object_values.video_assets import VideoAsset
from domain.abstractions.enums import MusicalGenre

class TrackEntity(BaseEntity):
    title: str
    duration_sec: int
    file_url: str
    track_number: int = 0
    genres: list[MusicalGenre] = Field(default_factory=list)
    artists: list[str] = Field(default_factory=list)
    album_id: ObjectID | None = None
    album_name: str | None = None
    video_assets: VideoAsset | None = None
    cover_image: str
