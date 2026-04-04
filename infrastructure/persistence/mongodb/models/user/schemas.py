from pydantic import BaseModel
from infrastructure.persistence.mongodb.models.enums import LanguageEnum
from infrastructure.persistence.mongodb.models.media.schemas import MediaQuality
from infrastructure.persistence.mongodb.models.notification.schemas import Notification

class Playback(BaseModel):
    auto_play: bool
    mono_audio: bool
    feedback_sounds: bool
    volume_level: int
    volume_normalization: bool

class Visibility(BaseModel):
    followers_and_following: bool
    playlists: bool
    recently_played_artists: bool

class Privacy(BaseModel):
    visibility: Visibility

class Settings(BaseModel):
    language: LanguageEnum = LanguageEnum.english
    playback: Playback | None = None
    privacy: Privacy | None = None
    media_quality: MediaQuality | None = None
    notifications: Notification | None = None
