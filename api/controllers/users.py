from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from application.services.users import UsersService
from api.dependencies.auth_dependency import get_users_pg_service, RoleChecker, get_current_user, get_users_mongo_service
from api.dtos.users import CreateUserDTO, UpdateUserDTO, UserResponse
from api.helpers.query_params import QueryParams

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/find/", response_model=List[UserResponse],status_code=status.HTTP_200_OK)
async def get_users(
    service: UsersService = Depends(get_users_mongo_service),
    params: QueryParams = None,
    #current_user: dict = Depends(RoleChecker(["admin"]))
):
    return await service.find(params=params)


@router.get("/{user_id}", response_model=Optional[UserResponse],status_code=status.HTTP_200_OK)
async def get_user(
    user_id: str,
    service: UsersService = Depends(get_users_pg_service),
    #current_user: dict = Depends(get_current_user)
):
    return await service.get_by_id(user_id)


@router.post("/", response_model=Optional[UserResponse],status_code=status.HTTP_201_CREATED)
async def create_user(
    user: CreateUserDTO,
    service: UsersService = Depends(get_users_pg_service),
    #current_user: dict = Depends(RoleChecker(["admin"]))
):
    return await service.create(user)


@router.patch("/{user_id}", response_model=UserResponse,status_code=status.HTTP_200_OK)
async def update_user(
    user_id: str,
    user: UpdateUserDTO,
    service: UsersService = Depends(get_users_pg_service),
    #current_user: dict = Depends(get_current_user)
):
    return await service.update(user_id, user)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(
    user_id: str,
    service: UsersService = Depends(get_users_pg_service),
    #current_user: dict = Depends(RoleChecker(["admin"]))
):
    return await service.delete(user_id)

@router.patch("/{user_id}/restore", status_code=status.HTTP_200_OK)
async def restore_user(
    user_id: str,
    service: UsersService = Depends(get_users_pg_service),
    #current_user: dict = Depends(RoleChecker(["admin"]))
):
    return await service.restore(user_id)
