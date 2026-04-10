from domain.interfaces.authentication import IJWTService, DataToCreateJwtToken
from application.services.users import UsersService
from domain.entities.user import UserEntity
from datetime import datetime
from domain.exceptions.base import UnauthorizedException
from domain.interfaces.repositories import IRoleUserRepository, IUsersRepositoryPostgres, IRoleRepository

class AuthenticationService:
    def __init__(self,
                 jwt_service: IJWTService,
                 users_service: UsersService,
                 role_user_repository: IRoleUserRepository,
                 user_repository_sql: IUsersRepositoryPostgres,
                 role_repository: IRoleRepository):
        self.jwt_service = jwt_service
        self.users_service = users_service
        self.user_repository_sql=user_repository_sql
        self.role_user_repository = role_user_repository
        self.role_repository=role_repository

    async def login(self, email: str, password: str) -> str:


        user = await self.user_repository_sql.get_by_email(email)
        if user is None:
            raise UnauthorizedException("Credenciales Invalidas")


        valid_password = await self.user_repository_sql.valid_password(user.id, password)
        if not valid_password:
            raise UnauthorizedException("Credenciales Invalidas")


        role_user = await self.role_user_repository.get_by_user_id(user.id)
        if role_user is None:
            raise UnauthorizedException("Credenciales Invalidas")

        role = await self.role_repository.get_by_id(role_user.role_id)
        if role is None:
            raise UnauthorizedException("Credenciales Invalidas")

        if role_user.is_active is not True:
            raise UnauthorizedException("Credenciales Invalidas")

        current_date = datetime.now()
        token_data = DataToCreateJwtToken(
            user_id=user.id,
            username=user.user_name,
            email=user.email,
            role=role.name,
            exp=current_date
        )
        return {"access_token":self.jwt_service.create_access_token(token_data)}


    async def register(self, user_entity: UserEntity) -> UserEntity:
        return await self.users_service.create(user_entity)
