from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from domain.abstractions.enums import AccountType

class CreateUserDTO(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    email: EmailStr
    account_type: AccountType = AccountType.free


class UpdateUserDTO(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    user_name: str | None = None
    email: EmailStr | None = None
    account_type: AccountType | None = None


class UserResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    user_name: str
    email: EmailStr
    account_type: str
    is_active: bool = True

    class Config:
        from_attributes = True
