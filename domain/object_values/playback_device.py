from pydantic import BaseModel

class PlaybackDevice(BaseModel):
    device_id: str
    device_name: str
    type: str
    model: str
    os: str
    ip_address: str
