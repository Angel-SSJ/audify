from pydantic import EmailStr
from pydantic import Field
from infrastructure.persistence.mongodb.models.abstractions.base import BaseModelMongo
from infrastructure.persistence.mongodb.models.artist.schemas import RecentlyPlayed
from infrastructure.persistence.mongodb.models.device.schemas import LinkedDevice
from infrastructure.persistence.mongodb.models.user.schemas import Settings
from app.validators.object_id import ObjectID
from infrastructure.persistence.mongodb.models.enums import AccountType

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
