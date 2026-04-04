from pydantic import BaseModel

class PlaybackInteractions(BaseModel):
    completed: bool
    skipped: bool
