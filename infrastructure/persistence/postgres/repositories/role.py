from infrastructure.persistence.postgres.repositories.base import BaseRepositoryPostgres
from infrastructure.persistence.postgres.models.role import RoleModel
from infrastructure.persistence.postgres.mappers.role import RoleSQLMapper
from domain.entities.role import RoleEntity
from domain.interfaces.repositories import IRoleRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class RoleRepositoryPostgres(BaseRepositoryPostgres[RoleEntity, RoleModel], IRoleRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model_class=RoleModel, mapper=RoleSQLMapper(), entity_name="Role")

    async def get_by_name(self, name: str) -> RoleEntity | None:
        try:
            stmt = select(self.model_class).where(self.model_class.name == name)
            result = await self.session.execute(stmt)
            model = result.scalar_one_or_none()
            return self.mapper.to_domain(model) if model else None
        except Exception as e:
            raise DomainException(str(e))
