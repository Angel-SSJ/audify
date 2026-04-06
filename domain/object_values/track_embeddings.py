from datetime import datetime
from pydantic import Field, BaseModel
from domain.object_values.artist_embeddings import ArtistEmbeddedList

class TrackEmbeddedPlaylist(BaseModel):
    track_id: str
    title: str = ''
    artist_name:str = ''
    duration_sec: int = 0
    cover_image: str = ''
    added_at: datetime = Field(default_factory=datetime.now)

class TrackEmbeddedAlbum(BaseModel):
    track_number: int = 0
    track_id: str
    title: str = ''
    duration_sec: int = 0
    artists: list[str] = Field(default_factory=list)
