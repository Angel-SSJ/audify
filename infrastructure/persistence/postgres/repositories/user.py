from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.persistence.postgres.repositories.base import BaseRepositoryPostgres
from infrastructure.persistence.postgres.models.user.model import UserModel
from infrastructure.persistence.postgres.mappers.user import UserSQLMapper
from domain.entities.user import UserEntity
from domain.interfaces.repositories import IUsersRepositoryPostgres
from sqlalchemy import select
import hashlib
from domain.exceptions.base import DomainException
from typing import Optional

class UserRepositoryPostgres(BaseRepositoryPostgres[UserEntity, UserModel], IUsersRepositoryPostgres):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model_class=UserModel, mapper=UserSQLMapper(), entity_name="User")

    async def create(self, domain_entity:UserEntity)->UserEntity:
        try:
            already_exists = await self.get_by_id(domain_entity.id)
            if already_exists:
                raise AlreadyExistsException(f"{self.entity_name} already exists")

            model_data = self.mapper.to_persistence(domain_entity)
            model = self.model_class(**model_data)
            self.session.add(model)
            await self.session.commit()
            await self.session.refresh(model)
            return self.mapper.to_domain(model)
        except Exception as e:
            await self.session.rollback()
            raise DomainException(str(e))
    async def get_by_email(self, email: str) -> Optional[UserEntity]:
        try:
            stmt = select(self.model_class).where(self.model_class.email == email, self.model_class.is_active == True)
            result = await self.session.execute(stmt)
            model = result.scalar_one_or_none()
            return self.mapper.to_domain(model) if model else None
        except Exception as e:
            await self.session.rollback()
            raise DomainException(str(e))

    def _hash_password(self, password: str) -> str:
        try:
            return hashlib.sha256(password.encode()).hexdigest()
        except Exception as e:
            raise DomainException(str(e))

    async def valid_password(self, user_id: str, password: str) -> bool:
        try:
            stmt = select(self.model_class).where(self.model_class.id == user_id)
            result = await self.session.execute(stmt)
            model = result.scalar_one_or_none()

            current_hashed_password = self._hash_password(password)
            hashed_password = self.mapper.to_domain(model).password
            return hashed_password == current_hashed_password if model else False


        except Exception as e:
            raise DomainException(str(e))
