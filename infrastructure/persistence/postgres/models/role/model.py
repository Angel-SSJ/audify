from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.persistence.postgres.models.base import Base
from infrastructure.persistence.postgres.models.user.schemas import UserRole

class RoleModel(Base):
    __tablename__ = "roles"
    name: Mapped[UserRole] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String, default="")
