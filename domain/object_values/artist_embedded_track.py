from pydantic import BaseModel

class ArtistEmbeddedTrack(BaseModel):
    artist_id: str
    name: str = ""
    role: str = ""
