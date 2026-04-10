from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from domain.interfaces.authentication import IJWTService
from infrastructure.security.jwt_service import JWTService
from infrastructure.persistence.postgres.postgres import get_pg_db
from infrastructure.persistence.postgres.repositories.user import UserRepositoryPostgres
from infrastructure.persistence.postgres.repositories.role_user import RoleUserRepositoryPostgres
from infrastructure.persistence.postgres.repositories.role import RoleRepositoryPostgres
from application.services.users import UsersService
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from domain.exceptions.base import UnauthorizedException, NotHavePermissionException
from domain.interfaces.repositories import IRoleUserRepository, IUsersRepositoryPostgres, IRoleRepository
from infrastructure.persistence.mongodb.repositories.users import UserRepository
from motor.motor_asyncio import AsyncIOMotorClient
from infrastructure.persistence.mongodb.mongo import get_mongo_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_jwt_service() -> IJWTService:
    return JWTService()

def get_role_user_repository(session: AsyncSession = Depends(get_pg_db)) -> IRoleUserRepository:
    return RoleUserRepositoryPostgres(session)

def get_user_repository_sql(session: AsyncSession = Depends(get_pg_db)) -> IUsersRepositoryPostgres:
    return UserRepositoryPostgres(session)

def get_role_repository(session: AsyncSession = Depends(get_pg_db)) -> IRoleRepository:
    return RoleRepositoryPostgres(session)

def get_users_pg_service(session: AsyncSession = Depends(get_pg_db)) -> UsersService:
    repo = UserRepositoryPostgres(session)
    return UsersService(repo)

def get_users_mongo_service(session: AsyncIOMotorClient = Depends(get_mongo_db)) -> UsersService:
    repo = UserRepository(session)
    return UsersService(repo)

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    jwt_service: IJWTService = Depends(get_jwt_service)
) -> dict:
    try:
        payload = jwt_service.verify_token(token)
        return payload
    except Exception as e:
        raise UnauthorizedException()

class RoleChecker:
    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: dict = Depends(get_current_user)):
       ''' if user.get("role") not in self.allowed_roles:
            raise NotHavePermissionException()
        return user'''
       return user

from application.services.authentication import AuthenticationService

def get_auth_service(
    jwt_service: IJWTService = Depends(get_jwt_service),
    users_service: UsersService = Depends(get_users_pg_service),
    role_user_repository: IRoleUserRepository = Depends(get_role_user_repository),
    user_repository_sql: IUsersRepositoryPostgres = Depends(get_user_repository_sql),
    role_repository: IRoleRepository = Depends(get_role_repository)
) -> AuthenticationService:
    return AuthenticationService(jwt_service, users_service,role_user_repository, user_repository_sql, role_repository)
