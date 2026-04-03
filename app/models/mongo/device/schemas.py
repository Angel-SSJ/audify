from pydantic import BaseModel, Field
from datetime import datetime

class LinkedDevice(BaseModel):
    device_id: str
    device_name: str
    type: str
    is_active: bool
    is_restricted: bool
    model: str
    os: str
    app_version: str
    registered_at: datetime = Field(default_factory=datetime.now)
    last_active_at: datetime | None = None
    ip_address: str
    offline_mode: bool

class PlaybackDevice(BaseModel):
    device_id: str
    device_name: str
    type: str
    model: str
    os: str
    ip_address: str
