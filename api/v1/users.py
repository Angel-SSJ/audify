from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from domain.entities.user import UserEntity
from application.services.users import UsersService
from infrastructure.persistence.mongodb.repositories.users import UserRepository
from api.dependencies.user_dependency import get_user_repository

router = APIRouter(prefix="/users", tags=["users"])


def get_users_service(
    repo: UserRepository = Depends(get_user_repository),
) -> UsersService:
    return UsersService(repo)


@router.get("/", response_model=List[UserEntity])
async def list_users(service: UsersService = Depends(get_users_service)):
    return await service.find(params=None)


@router.get("/{user_id}", response_model=UserEntity)
async def get_user(user_id: str, service: UsersService = Depends(get_users_service)):
    user = await service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("/", response_model=UserEntity, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserEntity, service: UsersService = Depends(get_users_service)):
    return await service.create(user)


@router.put("/{user_id}", response_model=UserEntity)
async def update_user(
    user_id: str,
    user: UserEntity,
    service: UsersService = Depends(get_users_service),
):
    updated = await service.update(user_id, user)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, service: UsersService = Depends(get_users_service)):
    deleted = await service.delete(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
