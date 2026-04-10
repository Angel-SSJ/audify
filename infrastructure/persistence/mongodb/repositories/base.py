from typing import TypeVar, Generic, Optional, List, Dict, Any, Type
from abc import ABC
from datetime import datetime
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorDatabase

from domain.interfaces.repositories import IBaseRepository
from domain.interfaces.mapper import IMapper
from domain.exceptions.base import DomainException, NotFoundException, AlreadyDeletedException, AlreadyExistsException
from api.helpers.object_id import ObjectID
from api.helpers.query_params import QueryParams, FieldFilter, SortOrder

D = TypeVar("D", bound=BaseModel)
P = TypeVar("P", bound=BaseModel)


class BaseRepositoryMongo(IBaseRepository[D], Generic[D, P]):

    def __init__(self, db: AsyncIOMotorDatabase, collection_name: str, mapper: IMapper[D, P], schema_class: Type[P], entity_name: str):
        self.mapper = mapper
        self.collection = db[collection_name]
        self.schema_class = schema_class
        self.entity_name = entity_name

    def _build_mongo_filters(self, filters: Dict[str, FieldFilter]) -> Dict:

        query: Dict[str, Any] = {}

        for field, f in filters.items():
            conditions: Dict[str, Any] = {}

            if f.eq       is not None: conditions["$eq"]     = f.eq
            if f.ne       is not None: conditions["$ne"]     = f.ne
            if f.gt       is not None: conditions["$gt"]     = f.gt
            if f.gte      is not None: conditions["$gte"]    = f.gte
            if f.lt       is not None: conditions["$lt"]     = f.lt
            if f.lte      is not None: conditions["$lte"]    = f.lte
            if f.in_      is not None: conditions["$in"]     = f.in_
            if f.nin      is not None: conditions["$nin"]    = f.nin
            if f.exists   is not None: conditions["$exists"] = f.exists
            if f.contains is not None:
                conditions["$regex"]   = f.contains
                conditions["$options"] = "i"

            query[field] = (
                conditions["$eq"]
                if list(conditions) == ["$eq"]
                else conditions
            )

        return query

    def _build_sort(self, sort_by: Optional[str], sort_order: SortOrder) -> Optional[list]:
        if not sort_by:
            return None
        direction = 1 if sort_order == SortOrder.ASC else -1
        return [(sort_by, direction)]

    def _to_entity(self, doc: Optional[Dict]) -> Optional[D]:
        if not doc:
            return None
        return self.mapper.to_domain(self.schema_class(**doc))

    async def get_by_id(self, id: str, is_active: bool = True) -> Optional[D]:
        try:
            doc = await self.collection.find_one({"_id": ObjectID(id), "is_active": is_active})
            return self._to_entity(doc) if doc else None
        except Exception as e:
            raise NotFoundException(self.entity_name)

    async def find(self, params: QueryParams) -> List[D]:
        try:
            if params is None:
                params = QueryParams()
            query = self._build_mongo_filters(params.filters)
            sort = self._build_sort(params.sort_by, params.sort_order)
            cursor = self.collection.find(query)
            if sort:
                cursor = cursor.sort(sort)
            cursor = cursor.skip(params.offset).limit(params.limit)
            docs = await cursor.to_list(length=params.limit)
            return [self._to_entity(doc) for doc in docs]
        except Exception as e:
            raise DomainException(str(e))

    async def create(self, entity: D) -> D:
        try:
            if await self.get_by_id(entity.id, is_active=True):
                raise AlreadyExistsException(self.entity_name)
            data = self.mapper.to_persistence(entity)
            data["created_at"] = datetime.utcnow()
            data["updated_at"] = datetime.utcnow()
            data["is_active"] = True
            result = await self.collection.insert_one(data)
            doc = await self.collection.find_one({"_id": result.inserted_id})
            return self._to_entity(doc)
        except Exception as e:
            raise DomainException(str(e))

    async def update(self, id: str, entity: Optional[D]) -> Optional[D]:
        try:
            if await self.get_by_id(id, is_active=False):
                    raise AlreadyDeletedException(self.entity_name)
            data = self.mapper.to_persistence(entity)
            data.pop("_id", None)
            data["updated_at"] = datetime.utcnow()
            result = await self.collection.find_one_and_update(
                {"_id": ObjectID(id)},
                {"$set": data},
                return_document=True,
            )
            return self._to_entity(result) if result else None
        except Exception as e:
            raise DomainException(str(e))

    async def delete(self, id: str) -> bool:
        try:
            if await self.get_by_id(id, is_active=False):
                raise AlreadyDeletedException(self.entity_name)

            data = {
                "is_active": False,
                "updated_at": datetime.utcnow(),
                "deleted_at": datetime.utcnow()
            }
            result = await self.collection.update_one(
                {"_id": ObjectID(id)},
                {"$set": data},
            )
            return result.modified_count > 0
        except Exception as e:
            raise DomainException(str(e))

    async def restore(self, id: str) -> bool:
        try:
            if not await self.get_by_id(id, is_active=False):
                raise AlreadyExistsException(self.entity_name)
            data = {
                "is_active": True,
                "updated_at": datetime.utcnow(),
            }
            result = await self.collection.update_one(
                {"_id": ObjectID(id)},
                {"$set": data},
            )
            return result.modified_count > 0
        except Exception as e:
            raise DomainException(str(e))
