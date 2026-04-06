from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ArtistEmbeddedResponse(BaseModel):
    artist_id: str
    name: str = ""
    role: str = ""


class VideoAssetResponse(BaseModel):
    canvas_url: str = ""
    video_duration_sec: int = 0
    available_qualities: List[str] = []

class CreateTrackDTO(BaseModel):
    title: str
    duration_ms: int
    album_id: str
    artist_id: str
    genre_id: str | None = None
    track_number: int = 0
    is_explicit: bool = False
    play_count: int = 0


class UpdateTrackDTO(BaseModel):
    title: str | None = None
    duration_ms: int | None = None
    album_id: str | None = None
    artist_id: str | None = None
    genre_id: str | None = None
    track_number: int | None = None
    is_explicit: bool | None = None
    play_count: int | None = None


class TrackResponse(BaseModel):
    id: str
    title: str
    duration_sec: int
    file_url: str = ""
    track_number: int = 0
    genres: List[str] = []
    artists: List[ArtistEmbeddedResponse] = []
    album_id: str | None = None
    album_name: str | None = None
    video_assets: Optional[VideoAssetResponse] = None
    cover_image: str = ""

    class Config:
        from_attributes = True
