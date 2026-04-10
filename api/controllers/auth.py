from fastapi import APIRouter, Depends, status
from api.dtos.auth import LoginDTO, RegisterDTO, TokenDTO
from application.services.authentication import AuthenticationService
from api.dependencies.auth_dependency import get_auth_service
from domain.entities.user import UserEntity
import uuid

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=TokenDTO)
async def login(data: LoginDTO, auth_service: AuthenticationService = Depends(get_auth_service)):
    token = await auth_service.login(data.email, data.password)
    return TokenDTO(access_token=token)

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(data: RegisterDTO, auth_service: AuthenticationService = Depends(get_auth_service)):
    user_entity = UserEntity(
        first_name=data.first_name,
        last_name=data.last_name,
        user_name=data.user_name,
        email=data.email,
        password=data.password,
        role=data.role,
        account_type="free",
    )
    return await auth_service.register(user_entity)
