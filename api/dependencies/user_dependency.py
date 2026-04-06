from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from infrastructure.persistence.mongodb.mongo import get_mongo_db
from infrastructure.persistence.mongodb.repositories.users import UserRepository
from application.services.users import UsersService


async def get_users_repository(
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
) -> UserRepository:
    return UserRepository(db)

def get_users_service(
    repo: UserRepository = Depends(get_users_repository),
) -> UsersService:
    return UsersService(repo)
