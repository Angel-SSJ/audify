from pydantic import BaseModel
from typing import Optional
from domain.abstractions.enums import LanguageEnum
from domain.object_values.media_quality import MediaQuality
from domain.object_values.notification import Notification

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
    playback: Optional[Playback] = None
    privacy: Optional[Privacy] = None
    media_quality: Optional[MediaQuality] = None
    notifications: Optional[Notification] = None
