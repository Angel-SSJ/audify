from pydantic import EmailStr
from app.models.mongo.abstractions.base import BaseModelMongo
from app.models.mongo.artist.schemas import RecentlyPlayed
from app.models.mongo.device.schemas import LinkedDevice
from app.models.mongo.user.schemas import Settings
from app.core.validators.object_id import ObjectID
from app.models.mongo.enums import AccountType

class User(BaseModelMongo[ObjectID]):
    first_name: str
    last_name: str = ''
    user_name: str = ''
    email: EmailStr
    total_followers: int = 0
    total_following: int = 0
    account_type: AccountType
    plan_id: str = ''
    recently_played: list[RecentlyPlayed] = []
    linked_devices: list[LinkedDevice] = []
    settings: Settings = Settings()
