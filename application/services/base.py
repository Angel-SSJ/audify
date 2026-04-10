from abc import ABC
from typing import TypeVar, Generic, Optional, Any, List
from pydantic import BaseModel
from domain.interfaces.repositories import IBaseRepository
from domain.exceptions.base import DomainException, AlreadyExistsException, NotFoundException

R = TypeVar("R", bound=IBaseRepository)
E = TypeVar("E", bound=BaseModel)


class BaseService(ABC, Generic[R, E]):
    def __init__(self, repository: R, entity_name: str):
        self.repository = repository
        self.entity_name = entity_name

    async def create(self, domain_entity: E) -> E:
        try:
            return await self.repository.create(domain_entity)
        except Exception as e:
            raise DomainException(str(e))

    async def get_by_id(self, id: str, is_active: bool = True) -> Optional[E]:
        try:
            result = await self.repository.get_by_id(id, is_active)
            if not result:
                raise NotFoundException(self.entity_name)
            return result
        except Exception as e:
            raise DomainException(str(e))

    async def find(self, params: Any) -> List[E]:
        try:
            result = await self.repository.find(params)
            if not result:
                raise NotFoundException(self.entity_name)
            return result
        except Exception as e:
            raise DomainException(str(e))

    async def update(self, id: str, entity: Optional[E]) -> Optional[E]:
        try:
            result = await self.repository.update(id, entity)
            if not result:
                raise NotFoundException(self.entity_name)
            return result
        except Exception as e:
            raise DomainException(str(e))

    async def delete(self, id: str) -> bool:
        try:
            result = await self.repository.delete(id)
            if not result:
                raise NotFoundException(self.entity_name)
            return result
        except Exception as e:
            raise DomainException(str(e))

    async def restore(self, id: str) -> bool:
        try:
            result = await self.repository.restore(id)
            if not result:
                raise NotFoundException(self.entity_name)
            return result
        except Exception as e:
            raise DomainException(str(e))
