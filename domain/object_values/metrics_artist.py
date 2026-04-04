from pydantic import BaseModel

class MetricsArtist(BaseModel):
    followers:int
    monthly_listeners:int
    global_rank:int
