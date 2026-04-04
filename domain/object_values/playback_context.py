from pydantic import BaseModel
from domain.abstractions.enums import PlaybackContextType
from app.validators.object_id import ObjectID

class PlaybackContext(BaseModel):
    type: PlaybackContextType
    id: ObjectID
