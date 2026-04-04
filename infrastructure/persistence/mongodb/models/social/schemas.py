from pydantic import BaseModel

class SocialLinksArtist(BaseModel):
    instagram: str = ''
    twitter: str = ''
    facebook: str = ''
    tiktok: str = ''
    youtube: str = ''
