from typing import Optional, Any, List
from domain.interfaces.repositories import IUsersRepository
from domain.entities.user import UserEntity
from application.services.base import BaseService

class UsersService(BaseService[IUsersRepository, UserEntity]):
    def __init__(self, users_repository: IUsersRepository):
        super().__init__(users_repository)
