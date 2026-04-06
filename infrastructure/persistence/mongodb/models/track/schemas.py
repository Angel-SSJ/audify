from datetime import datetime
from pydantic import Field, BaseModel
from app.validators.object_id import ObjectID
from infrastructure.persistence.mongodb.models.artist.schemas import ArtistEmbeddedList

class TrackEmbeddedPlaylist(BaseModel):
    track_id: ObjectID
    title: str = ''
    artist_name: str = ''
    duration_sec: int = 0
    cover_image: str = ''
    added_at: datetime = Field(default_factory=datetime.now)

class ArtistEmbeddedTrack(BaseModel):
    artist_id: ObjectID
    name: str = ""
    role: str = ""

class TrackEmbeddedAlbum(BaseModel):
    track_number: int = 0
    track_id: ObjectID
    title: str = ''
    duration_sec: int = 0
    artists:list[str] = Field(default_factory=list)
