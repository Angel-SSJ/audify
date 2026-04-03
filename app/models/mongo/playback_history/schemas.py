from pydantic import BaseModel
from app.core.validators.object_id import ObjectID
from app.models.mongo.enums import PlaybackContextType

class PlaybackInteractions(BaseModel):
    completed: bool
    skipped: bool

class PlaybackContext(BaseModel):
    type: PlaybackContextType
    id: ObjectID

class PlaybackDevice(BaseModel):
    device_id: str
    device_name: str
    type: str
    model: str
    os: str
    ip_address: str
