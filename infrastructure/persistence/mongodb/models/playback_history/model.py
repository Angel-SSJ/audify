from datetime import datetime
from infrastructure.persistence.mongodb.models.abstractions.base import BaseModelMongo
from app.validators.object_id import ObjectID
from infrastructure.persistence.mongodb.models.playback_history.schemas import (
    PlaybackDevice,
    PlaybackContext,
    PlaybackInteractions
)

class PlaybackHistory(BaseModelMongo[ObjectID]):
    user_id: ObjectID
    track_id: ObjectID
    played_at: datetime
    progress_ms: int
    track_duration_ms: int = 0
    percent_played: float = 0.0
    interactions: PlaybackInteractions | None = None
    context: PlaybackContext | None = None
    device: PlaybackDevice | None = None
    country_code: str
