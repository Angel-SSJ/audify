import hashlib
from typing import Optional, Any, List
from domain.interfaces.repositories import IUsersRepository
from domain.entities.user import UserEntity
from application.services.base import BaseService
from domain.exceptions.user import UserNotFoundException, UserAlreadyExistsException

class UsersService(BaseService[IUsersRepository, UserEntity]):
    def __init__(self, users_repository: IUsersRepository):
        super().__init__(users_repository)

    def _hash_password(self, password: str) -> str:
        try:
            return self.repository._hash_password(password)
        except Exception as e:
            raise DomainException(str(e))

    async def get_by_email(self, email: str) -> Optional[UserEntity]:
        try:
            return await self.repository.get_by_email(email)
        except Exception as e:
            raise DomainException(str(e))

    async def create(self, domain_entity: UserEntity) -> UserEntity:
        try:
            if domain_entity.hashed_password:
                domain_entity.hashed_password = self._hash_password(domain_entity.hashed_password)
            return await super().create(domain_entity)
        except Exception as e:
            raise DomainException(str(e))

    async def update(self, id: str, entity: Optional[UserEntity]) -> Optional[UserEntity]:
        try:

            if entity and entity.hashed_password:
                entity.hashed_password = self._hash_password(entity.hashed_password)

            return await super().update(id, entity)
        except Exception as e:
            raise DomainException(str(e))
