from pydantic import BaseModel, Field
from typing import Optional
from domain.object_values.track_embeddings import TrackEmbeddedPlaylist


class CreatePlaylistDTO(BaseModel):
    name: str
    description: str | None = None
    user_id: str
    track_ids: list[str] = Field(default_factory=list)
    is_public: bool = True


class UpdatePlaylistDTO(BaseModel):
    name: str | None = None
    description: str | None = None
    user_id: str | None = None
    track_ids: list[str] | None = None
    is_public: bool | None = None



class PlaylistResponse(BaseModel):
    id: str
    name: str
    description: str = ""
    owner_id: str
    is_public: bool = True
    followers_count: int = 0
    cover_image: str = ""
    tracks: list[TrackEmbeddedPlaylist] = []
    total_duration_sec: int = 0
    total_tracks: int = 0

    class Config:
        from_attributes = True
