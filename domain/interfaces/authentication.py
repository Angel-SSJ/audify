from abc import ABC, abstractmethod
from pydantic import BaseModel
from datetime import datetime

class DataToCreateJwtToken(BaseModel):
    user_id: str
    username: str
    email: str
    role: str
    exp: datetime

class IJWTService(ABC):
    @abstractmethod
    def create_access_token(self, data: DataToCreateJwtToken):
        pass

    @abstractmethod
    def verify_token(self, token: str):
        pass
