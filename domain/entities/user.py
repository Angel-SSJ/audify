from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from domain.abstractions.base import BaseEntity
from domain.object_values.setting import Settings
from domain.abstractions.enums import AccountType

class UserEntity(BaseEntity):
    first_name: str= Field(default="")
    last_name: str= Field(default="")
    user_name: str= Field(default="")
    email: EmailStr
    hashed_password: Optional[str] = None
    account_type: AccountType
    settings: Optional[Settings] = None
