from pydantic import BaseModel, Field

class ArtistEmbeddedList(BaseModel):
    names: list[str] = Field(default_factory=list)
