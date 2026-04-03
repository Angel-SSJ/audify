from pydantic import BaseModel
from app.models.mongo.enums import LanguageEnum
from app.models.mongo.media.schemas import MediaQuality
from app.models.mongo.notification.schemas import Notification

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
    playback: Playback
    privacy: Privacy
    media_quality: MediaQuality
    notifications:Notification
