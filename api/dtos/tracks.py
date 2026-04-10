from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from domain.abstractions.enums import MusicalGenre
from domain.object_values.video_assets import VideoAsset


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
    duration_sec: int
    file_url: str = ''
    track_number: int
    genres: list[MusicalGenre] = Field(default_factory=list)
    artists: list[ArtistEmbeddedResponse] = Field(default_factory=list)
    album_id: str
    album_name:str
    video_assets: VideoAsset | None = None
    cover_image: str = ''



class UpdateTrackDTO(BaseModel):
    title: str
    duration_sec: int
    file_url: str = ''
    track_number: int
    genres: list[MusicalGenre] = Field(default_factory=list)
    artists: list[ArtistEmbeddedResponse] = Field(default_factory=list)
    album_id: str
    album_name:str
    video_assets: VideoAsset | None = None
    cover_image: str = ''


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
