from pydantic import Field
from domain.abstractions.base import BaseEntity

class RoleEntity(BaseEntity):
    name: str = Field(default="")
    description: str = Field(default="")
