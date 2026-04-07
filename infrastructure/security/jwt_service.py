from api.config import settings
from datetime import datetime, timedelta
from domain.interfaces.authentication import DataToCreateJwtToken, IJWTService
import jwt
from domain.interfaces.repositories import IRoleUserRepository
from domain.exceptions.base import DomainException
from fastapi import HTTPException, status

class JWTService(IJWTService):
    def __init__(self):
        self.secret_key = settings.secret_key
        self.algorithm = settings.jwt_algorithm
        self.expire = settings.jwt_secret

    async def create_access_token(self, data: DataToCreateJwtToken):
        try:


            encode_data = data.model_dump()
            expire: datetime = datetime.now() + timedelta(minutes=self.expire)


            encode_data.update({"exp": expire})

            encoded_jwt: str = jwt.encode(encode_data, self.secret_key, algorithm=self.algorithm)
            return encoded_jwt
        except Exception as e:
            raise DomainException(str(e))

    async def verify_token(self, token: str)->bool:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])

            if payload.get("exp") < datetime.now():
                raise InvalidCredentialsException("Token expired")

            if payload.get("user_id") or payload.get("username") or payload.get("email") or payload.get("role") is None:
                raise InvalidCredentialsException("Token invalid")

            return payload
        except Exception as e:
            raise DomainException(str(e))
