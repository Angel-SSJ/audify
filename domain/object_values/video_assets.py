from pydantic import Field, BaseModel
from domain.abstractions.enums import VideoStreamingQualityResolution

class VideoAsset(BaseModel):
    canvas_url: str = ''
    video_duration_sec: int = 0
    available_qualities: list[VideoStreamingQualityResolution] = Field(default_factory=list)
