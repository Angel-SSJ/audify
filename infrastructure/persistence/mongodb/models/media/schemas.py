from pydantic import BaseModel, Field
from infrastructure.persistence.mongodb.models.enums import (
    DownloadQuality, 
    VideoStreamingQuality, 
    AudioStreamingQuality, 
    VideoStreamingQualityResolution
)

class MediaQuality(BaseModel):
    download: DownloadQuality = DownloadQuality.normal
    video_streaming: VideoStreamingQuality = VideoStreamingQuality.normal
    audio_streaming: AudioStreamingQuality = AudioStreamingQuality.normal

class VideoAsset(BaseModel):
    canvas_url: str = ''
    video_duration_sec: int = 0
    available_qualities: list[VideoStreamingQualityResolution] = Field(default_factory=list)

class ImagesProfileArtist(BaseModel):
    avatar: str = ''
    header: str = ''
