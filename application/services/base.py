from abc import ABC
from typing import TypeVar, Generic, Optional, Any, List
from pydantic import BaseModel
from domain.interfaces.repositories import IBaseRepository
from domain.exceptions.base import DomainException, AlreadyExistsException

R = TypeVar("R", bound=IBaseRepository)
E = TypeVar("E", bound=BaseModel)


class BaseService(ABC, Generic[R, E]):
    def __init__(self, repository: R):
        self.repository = repository

    async def create(self, domain_entity: E) -> E:
        try:
            return await self.repository.create(domain_entity)
        except Exception as e:
            raise DomainException(str(e))

    async def get_by_id(self, id: str) -> Optional[E]:
        try:
            return await self.repository.get_by_id(id)
        except Exception as e:
            raise DomainException(str(e))

    async def find(self, params: Any) -> List[E]:
        try:
            return await self.repository.find(params)
        except Exception as e:
            raise DomainException(str(e))

    async def update(self, id: str, entity: Optional[E]) -> Optional[E]:
        try:
            return await self.repository.update(id, entity)
        except Exception as e:
            raise DomainException(str(e))

    async def delete(self, id: str) -> bool:
        try:
            return await self.repository.delete(id)
        except Exception as e:
            raise DomainException(str(e))
