from pydantic import BaseModel, Field
from api.helpers.object_id import ObjectID
from infrastructure.persistence.mongodb.models.enums import ArtistRole

class ArtistTrack(BaseModel):
    artist_id: ObjectID = Field(default_factory=ObjectID)
    artist_name: str = ''
    role: ArtistRole = ArtistRole.primary

class RecentlyPlayed(BaseModel):
    artist_id: ObjectID = Field(default_factory=ObjectID)
    total_followers: int = 0
    artist_name: str = ''

class Aliases(BaseModel):
    items: list[str] = Field(default_factory=list)

class ArtistEmbeddedList(BaseModel):
    items: list[str] = Field(default_factory=list)
