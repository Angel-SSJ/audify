from domain.abstractions.base import BaseEntity

class RoleUserEntity(BaseEntity):
    user_id: str
    role_id: str
