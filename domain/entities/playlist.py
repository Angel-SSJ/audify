
from domain.abstractions.base import BaseEntity
from pydantic import Field
from domain.object_values.track_embeddings import TrackEmbeddedPlaylist
from app.validators.object_id import ObjectID

class PlaylistEntity(BaseEntity):
    name: str
    description: str = ''
    owner_id: ObjectID
    is_public: bool = True
    followers_count: int = 0
    cover_image: str = ''
    tracks: list[TrackEmbeddedPlaylist] = Field(default_factory=list)
    total_duration_sec: int = 0
    total_tracks: int = 0
