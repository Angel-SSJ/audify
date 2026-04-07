from typing import TypeVar, Generic, Optional, List, Type, Any
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from domain.interfaces.repositories import IBaseRepository
from domain.interfaces.mapper import IMapper
from domain.exceptions.base import NotFoundException
from datetime import datetime

D = TypeVar("D") # Domain Entity
M = TypeVar("M") # SQL Model

class BaseRepositoryPostgres(Generic[D, M], IBaseRepository[D]):
    def __init__(self, session: AsyncSession, model_class: Type[M], mapper: IMapper[D, Any], entity_name: str):
        self.session = session
        self.model_class = model_class
        self.mapper = mapper
        self.entity_name = entity_name

    async def get_by_id(self, id: str) -> Optional[D]:
        try:
            stmt = select(self.model_class).where(self.model_class.id == id, self.model_class.is_active == True)
            result = await self.session.execute(stmt)
            model = result.scalar_one_or_none()

            if not model:
                raise NotFoundException(f"{self.entity_name} not found")

            return self.mapper.to_domain(model) if model else None
        except Exception as e:
            await self.session.rollback()
            raise DomainException(str(e))

    async def create(self, domain_entity: D) -> D:
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

    async def update(self, id: str, domain_entity: Optional[D]) -> Optional[D]:
        try:
            if not domain_entity:
                return None

            already_exists = await self.get_by_id(domain_entity.id)
            if not already_exists:
                raise NotFoundException(f"{self.entity_name} not found")

            model_data = self.mapper.to_persistence(domain_entity)
            model_data.pop("id", None)
            model_data["updated_at"] = datetime.now()

            stmt = update(self.model_class).where(self.model_class.id == id).values(**model_data).returning(self.model_class)
            result = await self.session.execute(stmt)
            model = result.scalar_one_or_none()
            await self.session.commit()

            return self.mapper.to_domain(model) if model else None
        except Exception as e:
            await self.session.rollback()
            raise DomainException(str(e))

    async def delete(self, id: str) -> bool:
        try:
            already_exists = await self.get_by_id(id)
            if not already_exists:
                raise NotFoundException(f"{self.entity_name} not found")

            stmt = update(self.model_class).where(self.model_class.id == id).values(
                is_active=False,
                deleted_at=datetime.now(),
                updated_at=datetime.now()
            )
            result = await self.session.execute(stmt)
            await self.session.commit()
            return result.rowcount > 0
        except Exception as e:
            await self.session.rollback()
            raise DomainException(str(e))
