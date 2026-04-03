from pydantic import BaseModel, Field
from app.core.validators.object_id import ObjectID
from app.models.mongo.enums import ArtistRole, MusicalGenre

class ArtistTrack(BaseModel):
    artist_id: ObjectID
    artist_name: str
    role: ArtistRole

class RecentlyPlayed(BaseModel):
    artist_id: ObjectID
    total_followers: int
    artist_name: str

class Aliases(BaseModel):
    names: list[str] = Field(default_factory=list)

class ArtistEmbeddedList(BaseModel):
    names: list[str] = Field(default_factory=list)
