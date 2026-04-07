from pydantic import BaseModel, EmailStr

class LoginDTO(BaseModel):
    email: EmailStr
    password: str
    user_id: str
    user_name: str
    role: str

class RegisterDTO(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    email: EmailStr
    password: str
    role: str = "user"

class TokenDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"
