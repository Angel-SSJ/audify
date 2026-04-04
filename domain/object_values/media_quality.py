from enum import Enum
from pydantic import BaseModel
from domain.abstractions.enums import DownloadQuality, VideoStreamingQuality, AudioStreamingQuality


class MediaQuality(BaseModel):
    download: DownloadQuality = DownloadQuality.normal
    video_streaming: VideoStreamingQuality = VideoStreamingQuality.normal
    audio_streaming: AudioStreamingQuality = AudioStreamingQuality.normal
