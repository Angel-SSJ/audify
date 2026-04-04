from domain.abstractions.base import BaseEntity
from app.validators.object_id import ObjectID
from pydantic import Field
from datetime import datetime
from domain.object_values.playback_interactions import PlaybackInteractions
from domain.object_values.playback_context import PlaybackContext
from domain.object_values.playback_device import PlaybackDevice

class PlaybackHistoryEntity(BaseEntity):
    user_id: str
    track_id: str
    played_at: datetime
    progress_ms: int
    track_duration_ms: int = 0
    percent_played: float = 0.0
    interactions: PlaybackInteractions | None = None
    context: PlaybackContext | None = None
    device: PlaybackDevice | None = None
    country_code: str
