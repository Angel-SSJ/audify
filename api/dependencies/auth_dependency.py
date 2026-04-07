from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from domain.interfaces.authentication import IJWTService
from infrastructure.security.jwt_service import JWTService
from infrastructure.persistence.postgres.postgres import get_pg_db
from infrastructure.persistence.postgres.repositories.user import UserRepositoryPostgres
from application.services.users import UsersService
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from domain.exceptions.base import UnauthorizedException, NotHavePermissionException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_jwt_service() -> IJWTService:
    return JWTService()

def get_users_pg_service(session: AsyncSession = Depends(get_pg_db)) -> UsersService:
    repo = UserRepositoryPostgres(session)
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
        if user.get("role") not in self.allowed_roles:
            raise NotHavePermissionException()
        return user

from application.services.authentication import AuthenticationService

def get_auth_service(
    jwt_service: IJWTService = Depends(get_jwt_service),
    users_service: UsersService = Depends(get_users_pg_service)
) -> AuthenticationService:
    return AuthenticationService(jwt_service, users_service)
