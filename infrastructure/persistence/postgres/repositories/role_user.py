from infrastructure.persistence.postgres.repositories.base import BaseRepositoryPostgres
from infrastructure.persistence.postgres.models.role_user.model import RoleUserModel
from infrastructure.persistence.postgres.mappers.role_user import RoleUserSQLMapper
from domain.entities.role_user import RoleUserEntity
from domain.interfaces.repositories import IRoleUserRepository
from domain.exceptions.base import DomainException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class RoleUserRepositoryPostgres(BaseRepositoryPostgres[RoleUserEntity, RoleUserModel], IRoleUserRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model_class=RoleUserModel, mapper=RoleUserSQLMapper(), entity_name="RoleUser")

    async def get_by_user_id(self, user_id: str) -> RoleUserEntity | None:
        try:
            stmt = select(self.model_class).where(self.model_class.user_id == user_id)
            result = await self.session.execute(stmt)
            model = result.scalar_one_or_none()
            return self.mapper.to_domain(model) if model else None
        except Exception as e:
            raise DomainException(str(e))

    async def get_by_role_id(self, role_id: str) -> RoleUserEntity | None:
        try:
            stmt = select(self.model_class).where(self.model_class.role_id == role_id)
            result = await self.session.execute(stmt)
            model = result.scalar_one_or_none()
            return self.mapper.to_domain(model) if model else None
        except Exception as e:
            raise DomainException(str(e))
