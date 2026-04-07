from pydantic import BaseModel
from domain.abstractions.enums import PlaybackContextType
from api.helpers.object_id import ObjectID

class PlaybackContext(BaseModel):
    type: PlaybackContextType
    id: ObjectID
