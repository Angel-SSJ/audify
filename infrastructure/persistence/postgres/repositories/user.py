from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.persistence.postgres.repositories.base import BaseRepositoryPostgres
from infrastructure.persistence.postgres.models.user.model import UserModel
from infrastructure.persistence.postgres.mappers.user import UserSQLMapper
from domain.entities.user import UserEntity
from domain.interfaces.repositories import IUsersRepository

class UserRepositoryPostgres(BaseRepositoryPostgres[UserEntity, UserModel], IUsersRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model_class=UserModel, mapper=UserSQLMapper(), entity_name="User")

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
