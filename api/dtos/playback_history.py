from pydantic import BaseModel
from datetime import datetime

class CreatePlaybackHistoryDTO(BaseModel):
    user_id: str
    track_id: str
    played_at: datetime
    progress_ms: int
    track_duration_ms: int = 0
    percent_played: float = 0.0
    country_code: str


class UpdatePlaybackHistoryDTO(BaseModel):
    user_id: str | None = None
    track_id: str | None = None
    played_at: datetime | None = None
    progress_ms: int | None = None
    track_duration_ms: int | None = None
    percent_played: float | None = None
    country_code: str | None = None


class PlaybackHistoryResponse(BaseModel):
    id: str
    user_id: str
    track_id: str
    played_at: datetime
    progress_ms: int
    track_duration_ms: int = 0
    percent_played: float = 0.0
    interactions: dict | None = None
    context: dict | None = None
    device: dict | None = None
    country_code: str

    class Config:
        from_attributes = True
