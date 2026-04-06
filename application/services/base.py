from abc import ABC
from typing import TypeVar, Generic, Optional, Any, List
from pydantic import BaseModel
from domain.interfaces.repositories import IBaseRepository

R = TypeVar("R", bound=IBaseRepository)
E = TypeVar("E", bound=BaseModel)


class BaseService(ABC, Generic[R, E]):
    def __init__(self, repository: R):
        self.repository = repository

    async def create(self, domain_entity: E) -> E:
        return await self.repository.create(domain_entity)

    async def get_by_id(self, id: str) -> Optional[E]:
        return await self.repository.get_by_id(id)

    async def find(self, params: Any) -> List[E]:
        return await self.repository.find(params)

    async def update(self, id: str, entity: Optional[E]) -> Optional[E]:
        return await self.repository.update(id, entity)

    async def delete(self, id: str) -> bool:
        return await self.repository.delete(id)
