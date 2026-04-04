from pydantic import BaseModel, Field
from app.validators.object_id import ObjectID
from infrastructure.persistence.mongodb.models.enums import ArtistRole, MusicalGenre

class ArtistTrack(BaseModel):
    artist_id: ObjectID
    artist_name: str
    role: ArtistRole

class RecentlyPlayed(BaseModel):
    artist_id: ObjectID
    total_followers: int
    artist_name: str

class Aliases(BaseModel):
    items: list[str] = Field(default_factory=list)

class ArtistEmbeddedList(BaseModel):
    items: list[str] = Field(default_factory=list)
