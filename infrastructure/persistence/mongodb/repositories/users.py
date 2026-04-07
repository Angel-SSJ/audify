from motor.motor_asyncio import AsyncIOMotorDatabase
from domain.entities.user import UserEntity
from infrastructure.persistence.mongodb.models.user.model import User
from infrastructure.persistence.mongodb.mappers.user import UserMapper
from infrastructure.persistence.mongodb.repositories.base import BaseRepositoryMongo


class UserRepository(BaseRepositoryMongo[UserEntity, User]):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db=db, collection_name="users", mapper=UserMapper(), schema_class=User)


    async def create(self,entity:UserEntity)->UserEntity:
        data = self.mapper.to_persistence(entity)
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        data["is_active"] = True
        result = await self.collection.insert_one(data)
        doc = await self.collection.find_one({"_id": result.inserted_id})
        return self._to_entity(doc)

    async def update(self, id: str, entity: Optional[UserEntity]) -> Optional[UserEntity]:
        data = self.mapper.to_persistence(entity)
        data.pop("_id", None)
        data["updated_at"] = datetime.utcnow()
        result = await self.collection.find_one_and_update(
            {"_id": ObjectID(id)},
            {"$set": data},
            return_document=True,
        )
        return self._to_entity(result) if result else None

    async def delete(self, id: str) -> bool:
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
