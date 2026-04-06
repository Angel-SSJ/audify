from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from application.services.users import UsersService
from api.dependencies.user_dependency import get_users_service
from api.dtos.users import CreateUserDTO, UpdateUserDTO, UserResponse
from app.helpers.query_params import QueryParams

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/find/", response_model=List[UserResponse])
async def get_users(service: UsersService = Depends(get_users_service), params: QueryParams = None):
    return await service.find(params=params)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, service: UsersService = Depends(get_users_service)):
    user = await service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserDTO, service: UsersService = Depends(get_users_service)):
    return await service.create(user)


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: str,
    user: UpdateUserDTO,
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
