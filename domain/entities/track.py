from domain.abstractions.base import BaseEntity
from pydantic import Field
from datetime import datetime
from domain.object_values.video_assets import VideoAsset
from domain.abstractions.enums import MusicalGenre
from domain.object_values.artist_embedded_track import ArtistEmbeddedTrack

class TrackEntity(BaseEntity):
    title: str
    duration_sec: int
    file_url: str
    track_number: int = 0
    genres: list[MusicalGenre] = Field(default_factory=list)
    artists: list[ArtistEmbeddedTrack] = Field(default_factory=list)
    album_id: str | None = None
    album_name: str | None = None
    video_assets: VideoAsset | None = None
    cover_image: str
