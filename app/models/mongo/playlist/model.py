from pydantic import Field
from app.models.mongo.abstractions.base import BaseModelMongo
from app.core.validators.object_id import ObjectID
from app.models.mongo.track.schemas import TrackEmbeddedPlaylist

class Playlist(BaseModelMongo[ObjectID]):
    name: str
    description: str = ''
    owner_id: ObjectID
    is_public: bool = True
    followers_count: int = 0
    cover_image: str = ''
    tracks: list[TrackEmbeddedPlaylist] = Field(default_factory=list)
    total_duration_sec: int = 0
    total_tracks: int = 0
