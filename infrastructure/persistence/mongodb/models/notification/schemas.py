from pydantic import BaseModel

class NotificationTypeSugestion(BaseModel):
    playlists: bool
    artists: bool
    albums: bool

class NotificationType(BaseModel):
    new_features_and_tips: bool
    new_release: bool
    suggestions: NotificationTypeSugestion

class Notification(BaseModel):
    push_enabled: bool
    email_enabled: bool
    types: NotificationType
