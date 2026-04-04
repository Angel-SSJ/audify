from pydantic import BaseModel

class ImagesProfileArtist(BaseModel):
    avatar: str = ''
    header: str = ''
