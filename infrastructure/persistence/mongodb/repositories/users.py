from motor.motor_asyncio import AsyncIOMotorDatabase
from domain.entities.user import UserEntity
from infrastructure.persistence.mongodb.models.user.model import User
from infrastructure.persistence.mongodb.mappers.user import UserMapper
from infrastructure.persistence.mongodb.repositories.base import BaseRepositoryMongo


class UserRepository(BaseRepositoryMongo[UserEntity, User]):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db=db, collection_name="users", mapper=UserMapper(), schema_class=User)

