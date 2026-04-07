from pydantic import Field
from infrastructure.persistence.mongodb.models.abstractions.base import BaseModelMongo
from api.helpers.object_id import ObjectID
from infrastructure.persistence.mongodb.models.track.schemas import TrackEmbeddedPlaylist

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
