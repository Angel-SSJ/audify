from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.persistence.postgres.models.base import Base

class RoleUserModel(Base):
    __tablename__ = "user_roles"
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"))
    role_id: Mapped[str] = mapped_column(String, ForeignKey("roles.id"))
